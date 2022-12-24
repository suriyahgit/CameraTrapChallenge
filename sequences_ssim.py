from skimage.metrics import structural_similarity
import os
import cv2
import matplotlib.pyplot as plt

# Set the directory path
directory = '/home/dataknight/CameraTrapChallenge/data/test'

# Get a list of all files in the directory
files = os.listdir(directory)


grayscale = []
for file in files:
    # Check if the file is an image file
    if file.endswith(('.JPG', '.jpg')):
        # Read the image file using cv2.imread()
        image = cv2.imread(os.path.join(directory, file))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayscale.append(gray)

grayscale

(score, diff) = structural_similarity(grayscale[0], grayscale[2], full=True)
print(score)

sequences = []
# Iterate over the images and compare them to each other
for i in range(len(grayscale)):
    # Initialize a new sequence with the first image
    seq = [grayscale[i]]
    # Compare the current image to the rest of the images
    for j in range(i+1, len(grayscale)):
        ssim = structural_similarity(grayscale[i], grayscale[j])
        # If the structural similarity is above a certain threshold, add the image to the sequence
        if ssim > 0.6:
            seq.append(grayscale[j])
    # Add the sequence to the list of sequences
    sequences.append(seq)
    


fig, axes = plt.subplots(1, 2, figsize=(10, 7))
plt.sca(axes[0])
plt.imshow(grayscale[0])
plt.sca(axes[1])
plt.imshow(grayscale[2])
plt.show();