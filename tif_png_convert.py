'''
Goal: Convert a file containing .tif images to .png format

Input: Folder containing .tif images.
Output: Folder containing converted .png versions of the inputted .tif images.
'''

import os
import time
import czifile
import numpy as np
import cv2
from skimage import io
import argparse

# Create argument parser
parser = argparse.ArgumentParser(description="Convert .tif images to .png format.")
parser.add_argument("input_dir", type=str, help="Path to the input directory containing .tif images.")
parser.add_argument("output_dir", type=str, help="Path to the output directory where .png images will be saved.")

# Parse arguments
args = parser.parse_args()

# Read input and output directories from command line arguments
input_dir = args.input_dir
output_dir = args.output_dir

images = []

# if output directory does not exist, create one
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

start_time = time.time() # time how long algorithm takes to run

print("Starting image conversion...")
for file in os.listdir(input_dir):
    if '.tif' in file and '9.5' in file: # ensure is tif file and PGP 9.5
        img = np.array(cv2.imread(os.path.join(input_dir, file), 0))
        filename = file.replace(".tif", ".png")
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, img)
    
print("Conversion Complete!")
print("--- %s seconds ---" % (time.time() - start_time))