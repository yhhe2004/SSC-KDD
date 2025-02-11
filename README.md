
## Requirements

Python >= 3.9 | [PyTorch >=2.0](https://pytorch.org/) | [TorchData >=0.6.0](https://github.com/pytorch/data) | [PyG >=2.3](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html#)

## Environment Setup

    conda create -n css python=3.9;conda activate css;bash env.sh

## Usage
  
    unzip data/Amazon2014Baby_550_MMRec.zip -d data/Processed/Amazon2014Baby_550_MMRec/
    cd code/BACKBONE-augment
    python main.py --config configs/Amazon2014Baby_550_MMRec.yaml

