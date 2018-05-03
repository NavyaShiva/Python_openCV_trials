from PIL import Image
import os

im = Image.open(os.path.abspath("car")).convert('L')
img = im.crop((100,100,950,600))
img.show()
print(img)
im.show()
print(im)
