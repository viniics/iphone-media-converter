from PIL import Image
im = Image.open(r"test.png")
# The code opens an image file named "test.png" using the PIL library and displays it.
# Problem is, according to the doccumentation,  this file is saved somewhere in the hard drive.
im.show()
