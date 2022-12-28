# CameraTrapChallenge
(PROJECT UNDER DEVELOPMENT)

This project is part of the CameraTrapChallenge, which aims to develop algorithms for analyzing camera trap data.

## This Folder - 'coherant_sequence'
Contains code to identify coherant sequence of images from a group of images which contains several scenes using Structural Similarity Index (SSI) of Scikit-Image. SSI is a measure of the similarity between two images, based on the degree of structural distortion that would be required to align the images.

To use this code, you will need to create a virtual environment and install the necessary dependencies. To do this, navigate to the folder containing the code and run the following commands:
```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

## Project Goals
1. Identify coherent sequences of images (over time) for both Badger and Deer Dataset :ballot_box_with_check:
2. Locate the animals in the images (rough position) :ballot_box_with_check: Folder: coherant_sequence
3. Classify the animals (badger vs. deer) :ballot_box_with_check: Folder: custom-yolov7
4. Extend the BDD dataset with at least 2 additional species (at least 50 images each, day or day & night) of your choice (called BDD+)
5. Locate the animals in the images (alternative method)
6. Classify the animals into the min. 4 classes (alternative method)

## Project 

Using analytical and machine learning algorthms for animal detection from terrestrial remote sensing CameraTrap data of a National Park.
