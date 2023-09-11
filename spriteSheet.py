import os
from PIL import Image

# Image Directory
imgDir = './images/'

# List of files
imgFiles = os.listdir(imgDir)

# Sorting images
imgFiles.sort()

# Create list to store for export
imgLst = []

# Specify amount of rows
nRows = 5

# Specify amount of columns
nCols = 5

# Specify dimensions
outWidth = 1024
outHeight = 1024

# Loop through images and add them to image list
for file in imgFiles:
   image = Image.open(os.path.join(imgDir, file))
   imgLst.append(image)

maxWidth = nCols * imgLst[0].width
maxHeight = nRows * imgLst[0].height

# Creating new sprite sheet
imgOutput = Image.new('RGB', (maxWidth, maxHeight))

# Loop through images
for i, img in enumerate(imgLst):
   col = i % nCols
   row = i // nRows
   x = col * img.width
   y = row * img.height
   imgOutput.paste(image, (x, y))

# Resizing images from the list and save to new single sprite sheet PNG
imgOutput.resize((outWidth, outHeight)).save('spriteSheet.png')  