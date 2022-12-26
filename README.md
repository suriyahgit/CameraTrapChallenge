# CameraTrapChallenge
(PROJECT UNDER DEVELOPMENT)

## Project Goals
1. Identify coherent sequences of images (over time) for both Badger and Deer Dataset
2. Locate the animals in the images (rough position)
3. Classify the animals (badger vs. deer)
4. Extend the BDD dataset with at least 2 additional species (at least 50 images each, day or day & night) of your choice (called BDD+)
5. Locate the animals in the images (alternative method)
6. Classify the animals into the min. 4 classes (alternative method)

## Project 

###Internal Communication
The data folder still exists in the local project repository, so each time an user adds file to git, the folder that has the data is ignored, this was made possible by .gitignore. Data Folder existing as a part of .gitignore as the data used in this project is classified sensitive. Make sure the folder data is located inside the local project directory.

### Identify coherent sequences of images (over time) for both Badger and Deer Dataset
To identify sequences of images, first we need to start comparing two images to check whether they are identical or near identical, this can be done using analytical algorithm like Structural Similarity Index (SSIM)
	
--In Progress--
