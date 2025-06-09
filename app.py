from PIL import Image, ImageDraw
from pillow_heif import register_heif_opener
import os
# Register HEIF opener to handle HEIC files

register_heif_opener()

# Function to convert a single HEIC image to JPEG
def convert_img(img_name):
    im = Image.open(r"./files-to-convert/" + img_name)
    output_name = os.path.splitext(img_name)[0] + ".jpg"
    im.save(r"./converted/" + output_name, "JPEG")
    

# Batch conversion of HEIC files in a directory
def batch_convert():
    dir = "./files-to-convert"
    files = os.listdir(dir)
    total = len(files)
    index = 1
    for file in files:
        if file.lower().endswith(".heic"):  # Only process HEIC files
            print(f"Converting {file}...")
            convert_img(file)
            print(f"Success {index}/{total}")
            index += 1

batch_convert()