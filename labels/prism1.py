# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, prism1_height, prism1_sidelength
from plot import plot_surface

def construct_prism1(scaling, px, centre, prism1_sidelength, prism1_height):
    heightmap = np.zeros((px,px))

    #top-,left-,right- vertices
    top_x = centre
    top_y = centre - prism1_sidelength//2
    left_x = centre - prism1_sidelength//2
    left_y = centre + prism1_sidelength//2
    right_x = centre + prism1_sidelength//2
    right_y = left_y

    #Over each pixel
    for i in range(px):
        for j in range(px):
            # areas of subtriangles
            area_full = abs((
                            top_x*(left_y-right_y) + 
                             left_x*(right_y-top_y) + 
                             right_x*(top_y-left_y))/2
                             )

            area1 = abs((  
                        i*(left_y-right_y) + 
                        left_x*(right_y-j) + 
                        right_x*(j-left_y))/2
                         )

            area2 = abs((
                        top_x*(j-right_y) + 
                        i*(right_y-top_y) + 
                        right_x*(top_y-j))/2
                        )

            area3 = abs((
                        top_x*(left_y-j) + 
                        left_x*(j-top_y) + 
                        i*(top_y-left_y))/2
                        )

            #If the sum of the subtriangle areas equals the full triangle area, the point is inside the triangle
            if abs(area_full - (area1+area2+area3)) < 0.001:
                heightmap[j,i] = prism1_height

    #Normalise
    heightmap = heightmap/np.max(heightmap)
    
    return heightmap

if __name__ == "__main__":
    z = construct_prism1(scaling,px,centre,prism1_sidelength, prism1_height)
    plot_surface(X_mm, Y_mm, z, "prism1", zlim=1)