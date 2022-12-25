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

sequences = []
gray_seq = []

for i in range(len(files)):
    seq = {files[i]}
    gseq = [grayscale[i]]
    for j in range(len(files)):
        ssim = structural_similarity(grayscale[i], grayscale[j])
        if ssim > 0.6 and i!=j:
            seq.add(files[j])
            gseq.append(grayscale[j])
    sequences.append(seq)
    gray_seq.append(gseq)    

result_file_name = list()
for item in sequences:
    if item not in result_file_name:
        result_file_name.append(item)

result_file_name
