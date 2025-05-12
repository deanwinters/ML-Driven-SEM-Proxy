# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, cuboid1_size, cuboid1_height
from plot import plot_surface


def construct_cuboid(scaling,px,centre,length,height):
    #heightmap
    heightmap = np.zeros((px,px))

    #Loop for each pixel to set the height to 10mm for each pixel inside the face
    for i in range(px):
        for j in range(px):
            dx = i-centre
            dy = j-centre
            if abs(dx) <= length / 2 and abs(dy) <= length / 2:
                heightmap[i,j] = height

    # Normalise:
    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":
    heightmap = construct_cuboid(scaling,px,centre,cuboid1_size,cuboid1_height)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of Cuboid", zlim=1)