from PIL import Image
import os
import numpy as np
def get_cropped_image(image_path):

    im = Image.open(image_path).convert('L')
    cropped_img = im.crop((110,180,1000,600))
    return np.array(cropped_img)


if __name__ == "__main__":
    new_image = get_cropped_image(os.path.abspath("car"))
    print(new_image)
