# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm,  pyramid1_base, pyramid1_height
from plot import plot_surface

def construct_pyramid1(scaling,px,centre,length,height):     
    #heightmap
    heightmap = np.zeros((px,px))
    #central
    half_base = length/2
    #Iterate each px to map the height
    for i in range(px):
        for j in range(px):
            dx = abs(i-centre)
            dy = abs(j-centre)

            #For inside the base
            if dx <= half_base and dy <= half_base:
                #Distance from centre
                distance_from_center = max(dx,dy)
                #1:1 decrease (45deg)
                heightmap[i,j] = height*(1 - distance_from_center/half_base)
    #Normalise
    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":
    heightmap = construct_pyramid1(scaling,px,centre,pyramid1_base,pyramid1_height)
    plot_surface(X_mm, Y_mm, heightmap, "pyramid1", zlim=1)