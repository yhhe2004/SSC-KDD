
## 2025-02-06-14:38:33 


|  Attribute   |   Value   |
| :-------------: | :-----------: |
|  alpha  |   1.0    |
|  batch_size  |   2048    |
|  benchmark  |   False    |
|  BEST_FILENAME  |   best.pt    |
|  beta  |   1.0    |
|  beta1  |   0.9    |
|  beta2  |   0.999    |
|  CHECKPOINT_FILENAME  |   checkpoint.tar    |
|  CHECKPOINT_FREQ  |   1    |
|  CHECKPOINT_MODULES  |   ['model', 'optimizer', 'lr_scheduler']    |
|  CHECKPOINT_PATH  |   ./infos/lastfm-css-5/LastFM_330_MMRec/3    |
|  config  |   configs/LastFM_330_MMRec.yaml    |
|  dataset  |   LastFM_330_MMRec    |
|  DATA_DIR  |   data    |
|  ddp_backend  |   nccl    |
|  description  |   lastfm-css-5    |
|  device  |   cuda:3    |
|  early_stop_patience  |   1e+23    |
|  embedding_dim  |   64    |
|  epochs  |   500    |
|  eval_freq  |   5    |
|  eval_test  |   False    |
|  eval_valid  |   True    |
|  id  |   0206143826    |
|  log2console  |   True    |
|  log2file  |   True    |
|  LOG_PATH  |   ./logs/lastfm-css-5/LastFM_330_MMRec/0206143826    |
|  lr  |   0.005    |
|  mod_kappa  |   0    |
|  momentum  |   0.9    |
|  monitors  |   ['LOSS', 'Recall@1', 'Recall@10', 'Recall@20', 'NDCG@10', 'NDCG@20']    |
|  MONITOR_BEST_FILENAME  |   best.pkl    |
|  MONITOR_FILENAME  |   monitors.pkl    |
|  nesterov  |   False    |
|  noise_scale  |   0.0    |
|  num_layers  |   3    |
|  num_workers  |   4    |
|  optimizer  |   adam    |
|  ranking  |   full    |
|  resume  |   False    |
|  retain_seen  |   False    |
|  root  |   ../../data    |
|  SAVED_FILENAME  |   model.pt    |
|  scaling_factor  |   5.0    |
|  seed  |   1    |
|  shift_alpha  |   0.0    |
|  shift_beta  |   1.0    |
|  soc_kappa  |   0.75    |
|  SUMMARY_DIR  |   summary    |
|  SUMMARY_FILENAME  |   SUMMARY.md    |
|  tasktag  |   TaskTags.MATCHING    |
|  tfile  |   None    |
|  vfile  |   None    |
|  weight4mAdj  |   0.1    |
|  weight4mid  |   0.1    |
|  weight_decay  |   0.0001    |
|  which4best  |   NDCG@20    |
