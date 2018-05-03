#comparing 'mse' and 'ssim' methods accuracy  

from skimage.measure import structural_similarity as ssim
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image
import cv2


def mse(imageA, imageB):

    err = np.sum((imageA.astype("int") - imageB.astype("int"))**2)
    err = float(imageA.shape[0]*imageB.shape[1])

    return err


def compare_images(imageA, imageB, title):

    m = mse(imageA, imageB)
    s = ssim(imageA, imageB)

    fig = plt.figure(title)
    plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m,s))

    ax = fig.add_subplot(1,2,1)
    plt.imshow(imageA, cmap=plt.cm)
    plt.axis("off")

    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm)
    plt.axis("off")

    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB, cmap=plt.cm.)
    plt.axis("off")

    plt.show()
