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

(score, diff) = structural_similarity(grayscale[5], grayscale[10], full=True)
print(score)

fig, axes = plt.subplots(1, 2, figsize=(10, 7))
plt.sca(axes[0])
plt.imshow(grayscale[5])
plt.sca(axes[1])
plt.imshow(grayscale[10])
plt.show();
