from skimage.metrics import structural_similarity
import os
import cv2
import matplotlib.pyplot as plt

# Set the directory path
directory = 'data_ssim/test'

# Get a list of all files in the directory
files = os.listdir(directory)

scale_percent = 20
grayscale = []
for file in files:
    # Check if the file is an image file
    if file.endswith(('.JPG', '.jpg')):
        # Read the image file using cv2.imread()
        image = cv2.imread(os.path.join(directory, file))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        width = int(gray.shape[1] * scale_percent / 100)
        height = int(gray.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(gray, dim, interpolation = cv2.INTER_AREA)
        grayscale.append(resized)

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
coherant_seq = result_file_name

cs_image = []
i = 0
for segment in coherant_seq:
    add_images = []
    for file in coherant_seq[i]:
        if file.endswith(('.JPG', '.jpg')):
            image = cv2.imread(os.path.join(directory, file))
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            add_images.append(resized)
    i+=1
    cs_image.append(add_images)
print(i)
