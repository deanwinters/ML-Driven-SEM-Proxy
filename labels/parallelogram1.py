# CURRENTLY BROKEN

# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, parallelogram1_length, parallelogram1_height,parallelogram1_angle
from plot import plot_surface

def construct_parallelogram1(scaling, px, centre,parallelogram1_length,parallelogram1_height,parallelogram1_angle):
 
    heightmap = np.zeros((px, px))

    angle_rad = np.radians(parallelogram1_angle)
    #horizontal shift between top and bottom edges
    offset_px = parallelogram1_height / np.tan(angle_rad)

    #Base
    x0 = int(centre - parallelogram1_length/2)
    x1 = int(centre + parallelogram1_length/2)
    y_bottom = int(centre + parallelogram1_height/2)
    y_top = int(centre - parallelogram1_height/2)

    #Fill in
    for x in range(x0, x1):
        rel_x = (x-x0) / parallelogram1_length  # goes from 0 to 1 across the base
        y_top_edge = y_top + int(rel_x*offset_px)
        y_bottom_edge = y_bottom + int(rel_x*offset_px)

        for y in range(y_top_edge, y_bottom_edge):
            if 0 <= x < px and 0 <= y < px:
                heightmap[y, x] = parallelogram1_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap



if __name__ == "__main__":
    heightmap = construct_parallelogram1(scaling,px,centre,parallelogram1_length, parallelogram1_height, parallelogram1_angle)
    plot_surface(X_mm, Y_mm, heightmap,"parallelogram1", zlim=1)