# detect ArUco Marker using OpenCV
# https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/aruco_basics.html

import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def generate_markers():
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

    fig = plt.figure()
    nx = 4
    ny = 3
    for i in range(1, nx*ny+1):
        ax = fig.add_subplot(ny,nx, i)
        img = aruco.drawMarker(aruco_dict, i, 700)
        plt.imshow(img, cmap = mpl.cm.gray, interpolation = "nearest")
        ax.axis("off")

    plt.show()



if __name__ == "__main__":
    generate_markers()
