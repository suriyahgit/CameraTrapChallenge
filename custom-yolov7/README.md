# CameraTrapChallenge

This project is part of the CameraTrapChallenge, which aims to develop algorithms for analyzing camera trap data. In particular, this project focuses on using analytical and machine learning algorithms to detect and classify animals in camera trap data from a National Park.

## Locating, Detecting and Classifying Deer vs Badger
The yolov7 model is used to locate, detect, and classify deer versus badger in the camera trap data. The yolov7 model has been customized for this purpose and is included in the project folder. The following explains the process of preparing the data and customizing the model for this task:

### Preparing the Data and Setting Up the Training Environment
The image dataset has been divided into three folders: 65% for training ('train'), 20% for validation ('val'), and 15% for testing ('test') in a folder called data within the project directory. To use the model, place the training images in `~/data/train/images`, the validation images in `~/data/val/images`, and the test images in `~/data/test/images`.

Creating new conda environment for the dependencies to stay in peace without wrestling:-
```
conda create -n yolov7
```
Activating the conda environment:-
```
conda activate yolov7
```
### Labeling the Training Images
```
pip install labelImg
```
Open labelImg for labelling the dataset:-
```
labelImg
```
To label the training images, open the qt window and use the `Open Dir` button to select the `~/data/train/images` directory. Then, use the qt window to label each image one by one. To save the labels for each image, press the `Change Save directory` button and create a `labels` directory in `~/data/train/labels`. Make sure to select the format as `Yolo` in the qt window. This will allow the labeled images and their corresponding labels to be used for training the yolov7 model.

To install dependencies for training:-
```
pip install -r requirements_yolov7.txt
pip install -r requirements_gpu.txt
```

To avoid dependencies conflict, kindly make sure of using `numpy==1.23.5` and `scipy==1.5.0` instead of the latest version. For that you can use the below code.
```
pip install --upgrade numpy==1.23.5
pip install --upgrade scipy==1.5.0
```

### Customising the yolov7 model

To customize the yolov7 model for this project, the following changes should be made to the base model:

1. In the `~/cfg/training/` directory, duplicate the `yolov7.yaml` file and name it `yolov7-custom.yaml`. Then, change the number of classes to 2 to reflect the two classes in the image dataset.
2. In the `~/data directory`, duplicate the `coco.yaml` file and name it `custom_data.yaml`. Edit this file by removing the first four lines containing the download script for the cocodataset, modifying the directory paths to point to the training and validation datasets, and modifying the number of classes and class names to match the image dataset.
3. Download the pre-defined weights for running training from the official yolov7 repository on GitHub. The weights are named `yolov7.pt` and `yolov7-tiny.pt`, and should be placed in the root directory (`~/`). For this project, the `yolov7.pt` weights were used with the customizations described above to train the yolov7 model.

### Performing the Training

You can run the command now in the conda environment by `cd`-ing at the project folder for the training to be started:

```
python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt
```

Here is a breakdown of each of the arguments:

    `--workers`: This specifies the number of worker threads to use for data loading.
    `--device`: This specifies the device (e.g. CPU or GPU) to use for training.
    `--batch-size`: This specifies the number of images to include in each batch.
    `--epochs`: This specifies the number of epochs to train for. An epoch is a full pass through the training data.
    `--img`: This specifies the size of the images in the dataset. It looks like the images are 640 pixels wide and 640 pixels tall.
    `--data`: This specifies the path to a file containing data about the dataset.
    `--hyp`: This specifies the path to a file containing hyperparameters for the model.
    `--cfg`: This specifies the path to a configuration file for the model.
    `--name`: This specifies a name for the model.
    `--weights`: This specifies the path to a file containing pre-trained weights for the model.

After the training is completed, it generates a folder named `runs` which has the results and the trained weights. The weights file named `best.pt` from the `runs` folder is to be moved to `~/` and a test image can be brought to `~/` in my case `IMG_0117.JPG`.  For testing the image, the following command is used and the result will be generated at `~/runs/detect/exp/`.

```
python detect.py --weights best.pt --conf 0.5 --img-size 640 --source IMG_0117.JPG --view-img --no-trace
```

Here is a breakdown of each of the arguments:

    `--weights`: This specifies the path to a file containing weights for a machine learning model. These weights will be used to make predictions with the model.
    `--conf`: This specifies a minimum confidence threshold for predictions made by the model. Only predictions with a confidence level above this threshold will be included in the final output.
    `--img-size`: This specifies the size of the images that the model was trained on.
    `--source`: This specifies the path to an image file that the model will make predictions on.
    `--view-img`: This flag tells the script to display the image with the predictions overlaid on top.
    `--no-trace`: This flag tells the script to not display traceback information if an error occurs.

## Extending the model to the accomodate 2 additional species
(Under construction)

## Project Goals
1. Identify coherent sequences of images (over time) for both Badger and Deer Dataset :ballot_box_with_check:
2. **Locate the animals in the images (rough position) :ballot_box_with_check:**
3. **Classify the animals (badger vs. deer) :ballot_box_with_check:**
4. Extend the BDD dataset with at least 2 additional species (at least 50 images each, day or day & night) of your choice (called BDD+)
5. Locate the animals in the images (alternative method)
6. Classify the animals into the min. 4 classes (alternative method)

### References

1. Wang, C. Y., Bochkovskiy, A., & Liao, H. Y. M. (2022). YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors. arXiv preprint arXiv:2207.02696.
```
@misc{https://doi.org/10.48550/arxiv.2207.02696,
  doi = {10.48550/ARXIV.2207.02696},
  
  url = {https://arxiv.org/abs/2207.02696},
  
  author = {Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
  
  publisher = {arXiv},
  
  year = {2022},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```




