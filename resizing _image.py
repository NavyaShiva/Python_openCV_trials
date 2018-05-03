from PIL import Image
import os

def resize_image(Image_path):
    base_width = 300
    img = Image.open(Image_path)
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1])) * float(wpercent))
    img = img.resize((base_width, hsize), Image.ANTIALIAS)
    img.save('resized_image.jpg')
    a = Image.open('resized_image.jpg')
    return a

if __name__ == "__main__":
    resize = resize_image(os.path.abspath("car"))
    resize.show()
