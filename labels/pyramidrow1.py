# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, pyramidrow1_board_length,pyramidrow1_board_width, pyramidrow1_board_height, pyramidrow1_pyramid_base, pyramidrow1_angle
from plot import plot_surface

def construct_pyramidrow1(scaling,px, centre, board_length, board_width, board_height, pyramid_base, pyramid_slope_angle):
    heightmap = np.zeros((px,px))


    #Calculate board bounds
    x_start = max(centre - board_length//2, 0)
    x_end = min(centre + board_length//2, px)
    y_start = max(centre - board_width//2, 0)
    y_end = min(centre + board_width//2, px)

    # Set the board thickness in the heightmap
    heightmap[x_start:x_end, y_start:y_end] = board_height

    #Height based on sloping
    half_base = pyramid_base/2
    pyramid_height = half_base*np.tan(np.radians(pyramid_slope_angle))
    num_layers = int(pyramid_height)

    #Pyramid placement, centres corresponding to halves of half-lengths
    left_pyramid_centre_x = centre - board_length//4
    right_pyramid_centre_x = centre + board_length//4
    pyramid_centre_y = centre

    #Adding pyramid function
    def add_pyramid(cx, cy, base, height, num_layers):
        layer_step = height/num_layers
        base_step = base/(2*num_layers)
        
        for layer in range(num_layers):
            # Current layer dimensions
            current_height = board_height + layer*layer_step
            current_base = base - 2*layer*base_step
            
            # Calculate bounds for the current layer
            half_current_base = int(current_base/2)
            x_start = max(cx - half_current_base, 0)
            x_end = min(cx + half_current_base, px)
            y_start = max(cy - half_current_base, 0)
            y_end = min(cy + half_current_base, px)

            # Set heightmap values for this layer
            heightmap[x_start:x_end, y_start:y_end] = current_height

    # Add left and right pyramids
    add_pyramid(left_pyramid_centre_x, pyramid_centre_y, pyramid_base, pyramid_height, num_layers)
    add_pyramid(right_pyramid_centre_x, pyramid_centre_y, pyramid_base, pyramid_height, num_layers)

    #Normalise
    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_pyramidrow1(scaling,px,centre, pyramidrow1_board_length,pyramidrow1_board_width, pyramidrow1_board_height,
                                      pyramidrow1_pyramid_base, pyramidrow1_angle)
    plot_surface(X_mm, Y_mm, heightmap, "pyramidrow1", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
