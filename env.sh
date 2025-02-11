#conda create -n css python=3.9;conda activate css;bash env.sh

pip install freerec==0.8.7
conda install pytorch=2.1 torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia 
conda install pandas tqdm matplotlib torchdata=0.7.1 pyg -c pyg
pip install scikit-learn
