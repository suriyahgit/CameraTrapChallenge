from skimage.metrics import structural_similarity
import numpy as np
from PIL import Image
import glob

# Get a list of all image files in the directory
image_files = glob.glob('/data/test/*.jpg')

# Load the images into a list
images = []
for file in image_files:
    image = Image.open(file)
    images.append(image)

# Create a list to hold the sequences of images
sequences = []

# Iterate over the images and compare them to each other
for i in range(len(images)):
    # Initialize a new sequence with the first image
    seq = [images[i]]
    # Compare the current image to the rest of the images
    for j in range(i+1, len(images)):
        ssim = structural_similarity(images[i], images[j])
        # If the structural similarity is above a certain threshold, add the image to the sequence
        if ssim > 0.8:
            seq.append(images[j])
    # Add the sequence to the list of sequences
    sequences.append(seq)
