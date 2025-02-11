
## 2025-02-07-11:06:15 


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
|  CHECKPOINT_PATH  |   ./infos/ele-css-5/Amazon2014Electronics_550_MMRec/3    |
|  config  |   configs/Amazon2014Electronics_550_MMRec.yaml    |
|  dataset  |   Amazon2014Electronics_550_MMRec    |
|  DATA_DIR  |   data    |
|  ddp_backend  |   nccl    |
|  description  |   ele-css-5    |
|  device  |   cuda:3    |
|  early_stop_patience  |   1e+23    |
|  embedding_dim  |   64    |
|  epochs  |   500    |
|  eval_freq  |   5    |
|  eval_test  |   False    |
|  eval_valid  |   True    |
|  id  |   0207110611    |
|  log2console  |   True    |
|  log2file  |   True    |
|  LOG_PATH  |   ./logs/ele-css-5/Amazon2014Electronics_550_MMRec/0207110611    |
|  lr  |   0.001    |
|  mod_kappa  |   5    |
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
|  seed  |   2    |
|  shift_alpha  |   0.0    |
|  shift_beta  |   0.75    |
|  soc_kappa  |   0    |
|  SUMMARY_DIR  |   summary    |
|  SUMMARY_FILENAME  |   SUMMARY.md    |
|  tasktag  |   None    |
|  tfile  |   textual_modality.pkl    |
|  vfile  |   visual_modality.pkl    |
|  weight4mAdj  |   0.1    |
|  weight4mid  |   0.0    |
|  weight_decay  |   0.001    |
|  which4best  |   NDCG@20    |
