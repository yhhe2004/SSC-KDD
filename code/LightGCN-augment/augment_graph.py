
import numpy as np
import pandas as pd
import torch, os
import torch.nn as nn
import torch.nn.functional as F
import freerec
from freerec.data.tags import USER, ITEM, TIMESTAMP, ID
from torch_geometric.utils import scatter
from sklearn.decomposition import PCA

def get_graph(dataset, cfg, user_count, item_count):
    interactions = dataset.train().to_bigraph((USER, ID), (ITEM, ID), edge_type='U2I')['U2I'].edge_index
    interactions[1] += user_count
    i2u = torch.flip(interactions, dims=[0])
    edge_index = torch.cat([interactions, i2u], dim=1)
    edge_weight = torch.ones_like(edge_index[0])
    
    if cfg.mod_kappa > 0:
        mod_edges, mod_weights = load_feats(dataset.path, cfg)
        mod_edges += user_count
        edge_index = torch.cat([edge_index, mod_edges], dim=1)
        edge_weight = torch.cat([edge_weight, mod_weights], dim=0)

    if cfg.soc_kappa > 0:
        social_edges = pd.read_csv(os.path.join(dataset.path, 'trust_mat.txt'), sep='\t', header=0)
        social_edges = torch.tensor(social_edges.to_numpy()).T
        noise = torch.randint(0, user_count, social_edges.shape)
        noise_ratio = torch.bernoulli(torch.ones_like(social_edges) * cfg.noise_scale).to(torch.bool)
        social_edges = torch.where(noise_ratio, noise, social_edges)
        social_edges = torch.unique(torch.cat([social_edges, torch.flip(social_edges, dims=[0])], dim=1), dim=1)
        social_weights = torch.ones_like(social_edges[0]) * cfg.soc_kappa
        edge_index = torch.cat([edge_index, social_edges], dim=1)
        edge_weight = torch.cat([edge_weight, social_weights], dim=0)

    rows, cols = edge_index[0], edge_index[1]
    row_deg = 1.e-7 + scatter(edge_weight, rows, dim=0, dim_size=user_count+item_count)
    row_deg = row_deg.pow(-0.5)
    col_deg = 1.e-7 + scatter(edge_weight, cols, dim=0, dim_size=user_count+item_count)
    col_deg = col_deg.pow(-0.5)
    edge_weight = edge_weight * row_deg[rows] * col_deg[cols]

    eye_tensor = torch.tile(torch.arange(0, user_count+item_count), (2, 1))
    edge_index = torch.cat([edge_index, eye_tensor], dim=1)
    edge_weight = torch.cat([edge_weight, - torch.ones_like(eye_tensor[0]) * cfg.shift_mu]) / cfg.shift_delta

    A = torch.sparse_coo_tensor(
            edge_index, edge_weight.to(dtype=torch.float32),
            size=(user_count+item_count, user_count+item_count),
            device=cfg.device
        )
    return A.to_sparse_csr()

def load_feats(path: str, cfg):
    from freerec.utils import import_pickle
    if cfg.vfile:
        vFeats = import_pickle(
            os.path.join(path, cfg.vfile)
        )
        vFeats += torch.randn_like(vFeats) * cfg.noise_scale
        vedges, vweight = get_knn_graph(vFeats, cfg.mod_kappa)
    if cfg.tfile:
        tFeats = import_pickle(
            os.path.join(path, cfg.tfile)
        )
        tFeats += torch.randn_like(tFeats) * cfg.noise_scale
        tedges, tweight = get_knn_graph(tFeats, cfg.mod_kappa)

    if cfg.vfile and cfg.tfile:
        E = torch.cat([vedges, tedges], dim=1)
        W = torch.cat([vweight * cfg.weight4mAdj, tweight * (1 - cfg.weight4mAdj)], dim=0)
    elif cfg.vfile:
        E = vedges
        W = vweight
    elif cfg.tfile:
        E = tedges
        W = tweight
    else:
        raise

    return E, W

def get_knn_graph(features: torch.Tensor, knn_k):
    pca = PCA(n_components=min(200, features.shape[-1]))
    new = pca.fit_transform(features)
    features = torch.tensor(new, device=features.device)
    features = F.normalize(features, dim=-1) # (N, D)
    sim = features @ features.t() # (N, N)
    #sim = torch.exp((sim-1)/cfg.temperature)
    edge_index, _ = freerec.graph.get_knn_graph(
        sim, knn_k, symmetric=True
    )
    edge_weight = torch.ones_like(edge_index[0])
    return edge_index, edge_weight