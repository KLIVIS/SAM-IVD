#  SAM for Industrial Vision Detection (SAM-IVD)

This repository contains a dataset for mobile phone screen defects called Phone_Screen,  a set of utility scripts for data preprocessing and manipulation and  evaluating the performance of SAM on industrial defects. It's an open-source toolkit for evaluating SAM in defect data.

##  Dataset

The Phone_Screen dataset includes image data with corresponding defect segmentation masks. You can find the dataset in the following path:

`SAM-IVD/dataset/phone_screen512x512_ade`

Our Phone_Screen dataset was collected from factories involved in mobile screen manufacturing and is designed for tasks related to mobile screen defect segmentation. To accommodate hardware limitations, we performed preprocessing on the dataset. Initially, we divided each image, originally sized at 5120 $\times$ 5120 pixels, into smaller blocks of 512 $\times$ 512 pixels. Subsequently, we applied data augmentation techniques such as rotation and flipping to each of these blocks, thereby increasing the diversity within our training set. In order to ensure sample balance and improve the generalization of our model, we included all blocks containing defects in the preprocessed training set, while only including a small portion of defect-free blocks.

The  file structure of this dataset:

```
-─SAM-IVD
    └─dataset
        └─phone_screen512x512_ade
            ├─annotations
            │  ├─training
            │  ├─validation
            │  └─可视化标签
            └─images
                ├─training
                └─validation
```

The dataset comprises three classes of pixel-level annotations, including scratches, bubbles, and dust caused by environmental factors, as shown in the following figure. The presence of scratches and bubbles can negatively impact the appearance and usability of the mobile screen. These defects generally span tens to hundreds of pixels, significantly smaller than the original image scale of 5120$\times$5120. Moreover, due to subtle contrast variations when compared to the background, the observation and detection of these defects pose considerable challenges. Although dust is not classified as a defect, its presence can interfere with the accurate detection of scratches and bubbles, leading to the occurrence of false positive defect identifications. Consequently, we consider dust as an additional target for detection and provide corresponding annotations.

![phone_screen](https://raw.gitmirror.com/da5sdasddasa/image/main/202311231630087.jpg)

## Utils

* `json2mask.py`: Converts JSON-format labels into PNG-format mask images.
* `mat2mask.py`: Converts MATLAB (.mat) format masks into PNG-format images.
* `mask_filter.py`: Filters images by removing those without any defects based on their masks.

* `mask_move.py`: Moves files to their respective folders based on an Intersection over Union (IoU) threshold.

* `mvtec_dataloader.py`: Loads images and labels from the MVTec dataset for training or testing machine learning models.

##  Evaluation

* `sam_everything.ipynb`: This file contains implementations and example code for evaluating SAM in Everything mode with different backbones, grid points and metrics.

* `sam_prompt.ipynb`: This file contains implementations and example code for evaluating SAM in interactive mode with different backbones,  prompt strategies and metrics.

  

## Getting Started

To get started, follow the steps below:

1. Clone this repository to your local machine.


```bash
git clone https://github.com/KLIVIS/SAM-IVD.git
cd SAM-IVD
```

2. Installation of SAM

The code requires `python>=3.8`, as well as `pytorch>=1.7` and `torchvision>=0.8`. Please follow the instructions [here](https://pytorch.org/get-started/locally/) to install both PyTorch and TorchVision dependencies. Installing both PyTorch and TorchVision with CUDA support is strongly recommended.

Install Segment Anything:

```
pip install git+https://github.com/facebookresearch/segment-anything.git
```

or clone the repository locally and install with

```
git clone git@github.com:facebookresearch/segment-anything.git
cd segment-anything; pip install -e .
```

3. 


### Citation

If you use our Our Phone_Screen dataset or find our work useful in your research, please use the following BibTeX entry.

```

```
