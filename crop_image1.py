from PIL import Image
import os

image_obj = Image.open(os.path.abspath("entry_exit.jpg"))
area = (100, 100, 100, 100)
cropped_image = image_obj.crop(area)

image_obj.show()
#assert isinstance(cropped_image, object)
cropped_image.show()

