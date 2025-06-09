from PIL import Image, ImageDraw
from pillow_heif import register_heif_opener
import os
# Register HEIF opener to handle HEIC files

register_heif_opener()

# Directory paths for input HEIC files and output JPEG files
input_dir = "./files-to-convert/"
output_dir = "./converted/"

# Function to convert a single HEIC image to JPEG
def convert_img(img_name):
    im = Image.open(input_dir+ img_name)
    output_name = os.path.splitext(img_name)[0] + ".jpg"
    im.save(output_dir + output_name, "JPEG")
    

# Batch conversion of HEIC files in a directory
def batch_convert():
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    files = os.listdir(input_dir)
    heic_files = [f for f in files if f.lower().endswith(".heic")]
    total = len(heic_files)
    index = 1
    for file in heic_files:
        print(f"Converting {file}...")
        convert_img(file)
        print(f"Success {index}/{total}")
        index += 1

batch_convert()