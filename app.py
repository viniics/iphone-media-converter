from PIL import Image, ImageDraw
im = Image.open(r"test.png")
# The code opens an image file named "test.png" using the PIL library and displays it as a new temporary file.
converted = ImageDraw.Draw(im)
converted.text((50, 50), "As a JPG file", fill=(0, 0, 0))
im = im.convert("RGB")
im.save("test-converted.jpg", "JPEG")
im.show()

