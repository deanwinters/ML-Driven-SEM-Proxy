import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, draftcuboid3_base_length, draftcuboid3_base_width, draftcuboid3_height, draftcuboid3_angle,draftcuboid3_hex_radius, draftcuboid3_hex_height
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_draftcuboid3(scaling, px, centre, base_length, base_width, height, draft_angle, hex_radius, hex_height):
    heightmap = np.zeros((px,px))

    #Number of layers
    num_layers = int(height)
    height_step = height/num_layers

    #Calculate new rectangle for each layer
    for layer in range(num_layers):
        current_height = layer*height_step

        reduction = current_height  # since tan45=1, reduction = current_height

        #Shave both sides for each draft reduction
        current_length = base_length - 2*reduction
        current_width = base_width - 2*reduction

        #Convert dimensions to pixel grid units
        length_px = int(current_length)
        width_px = int(current_width)

        #Positions to update heightmap
        x_start = max(centre - length_px//2, 0)
        x_end = min(centre + length_px //2, px)
        y_start = max(centre - width_px//2, 0)
        y_end = min(centre + width_px//2, px)
        heightmap[x_start:x_end, y_start:y_end] = current_height

    # Add a hexagonal prism on top of the draft cuboid, define final heights
    hex_radius_px = int(hex_radius) 
    top_cuboid_height = height
    hex_top_height = top_cuboid_height+hex_height

    #Create hex vertices
    angles = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 angles for hexagon
    x_vertex = centre + hex_radius_px*np.cos(angles)
    y_vertex = centre + hex_radius_px*np.sin(angles)

    # Convert vertices to pixel grid indices
    x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
    y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

    #Polygon for each layer
    rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
    
    #Set height
    heightmap[rr, cc] = hex_top_height
    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_draftcuboid3(scaling,px,centre, draftcuboid3_base_length, draftcuboid3_base_width, draftcuboid3_height, draftcuboid3_angle,
                                       draftcuboid3_hex_radius, draftcuboid3_hex_height)
    plot_surface(X_mm, Y_mm, heightmap, "draftcuboid3", zlim=2.5)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
