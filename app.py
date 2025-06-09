from PIL import Image, ImageDraw
from pillow_heif import register_heif_opener
# Register HEIF opener to handle HEIC files

register_heif_opener()

im = Image.open(r"TEST.HEIC")
im.save("test-converted.png", "PNG")