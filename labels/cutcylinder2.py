# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, cutcylinder2_radius, cutcylinder2_height
from plot import plot_surface

def construct_cutcylinder2(scaling,px,centre,cutcylinder2_radius,cutcylinder2_height):     
    #Empty heightmap
    heightmap = np.zeros((px,px))

    # Loop over each pixel to calculate the height
    for i in range(px):
        #Get radial distance from centre
        for j in range(px):
            dx = i-centre
            dy = j-centre
            distance_from_centre = np.sqrt(dx**2+dy**2)
            #Inside radius:
            if distance_from_centre <= cutcylinder2_radius and dx>=0 and dy>=0:
                heightmap[i,j] =  cutcylinder2_height
    heightmap = heightmap/np.max(heightmap)
    #heightmap = np.expand_dims(heightmap, axis=0)  #gtb heightmap becomes (1, 128, 128)
    return heightmap

if __name__ == "__main__":

    heightmap = construct_cutcylinder2(scaling,px,centre,cutcylinder2_radius, cutcylinder2_height)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of Cylinder1", zlim=1)
    #step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)

    