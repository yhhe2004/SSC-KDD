
## 2025-02-08-11:30:14 


|  Attribute   |   Value   |
| :-------------: | :-----------: |
|  batch_size  |   2048    |
|  benchmark  |   False    |
|  BEST_FILENAME  |   best.pt    |
|  beta1  |   0.9    |
|  beta2  |   0.999    |
|  CHECKPOINT_FILENAME  |   checkpoint.tar    |
|  CHECKPOINT_FREQ  |   1    |
|  CHECKPOINT_MODULES  |   ['model', 'optimizer', 'lr_scheduler']    |
|  CHECKPOINT_PATH  |   ./infos/baby-css-5/Amazon2014Baby_550_MMRec/2    |
|  config  |   configs/Amazon2014Baby_550_MMRec.yaml    |
|  dataset  |   Amazon2014Baby_550_MMRec    |
|  DATA_DIR  |   data    |
|  ddp_backend  |   nccl    |
|  description  |   baby-css-5    |
|  device  |   cuda:2    |
|  early_stop_patience  |   1e+23    |
|  embedding_dim  |   64    |
|  epochs  |   500    |
|  eval_freq  |   5    |
|  eval_test  |   False    |
|  eval_valid  |   True    |
|  id  |   0208113009    |
|  log2console  |   True    |
|  log2file  |   True    |
|  LOG_PATH  |   ./logs/baby-css-5/Amazon2014Baby_550_MMRec/0208113009    |
|  lr  |   0.005    |
|  mod_kappa  |   10    |
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
|  seed  |   1    |
|  shift_alpha  |   0.05    |
|  shift_beta  |   0.75    |
|  soc_kappa  |   0    |
|  SUMMARY_DIR  |   summary    |
|  SUMMARY_FILENAME  |   SUMMARY.md    |
|  tasktag  |   None    |
|  tfile  |   textual_modality.pkl    |
|  vfile  |   visual_modality.pkl    |
|  weight4mAdj  |   0.1    |
|  weight_decay  |   1e-06    |
|  which4best  |   NDCG@20    |
