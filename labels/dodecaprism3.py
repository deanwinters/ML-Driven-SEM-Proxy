# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, dodecaprism3_radius, dodecaprism3_height,dodecaprism3_top_radius,dodecaprism3_cuboid_height, dodecaprism3_cuboid_length
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_dodecaprism3(scaling,px, centre, base_radius, height, top_radius, cuboid_length, cuboid_height):
    heightmap = np.zeros((px,px))
    
    #split into layers
    num_layers = int(height)
    height_step = height/num_layers

    for layer in range(num_layers):
        # height for layer
        current_height = layer*height_step
        #associated radius
        current_radius = base_radius + (top_radius-base_radius) * (current_height/height)

        # Calculate vertices for the dodecagon at this layer
        angles = np.linspace(0, 2*np.pi, 13)[:-1]  # 12 angles for dodecagon
        x_vertex = centre + current_radius*np.cos(angles)
        y_vertex = centre + current_radius*np.sin(angles)

        # Convert vertices to pixel grid indices
        x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
        y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

        #Layered polygon fit
        rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
        
        # Set heightmap values inside the dodecagon for this layer's height
        heightmap[rr,cc] = current_height
        
        # Define the pixel range for the cuboid centered on `centre`
        x_start = max(centre - cuboid_length//2, 0)
        x_end = min(centre + cuboid_length//2, px)
        y_start = max(centre - cuboid_length//2, 0)
        y_end = min(centre + cuboid_length//2, px)
        
        heightmap[x_start:x_end, y_start:y_end] = current_height+cuboid_height  # Normalize to prism height

    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":
    # Use parameters from external sources
    heightmap = construct_dodecaprism3(scaling, px, centre, dodecaprism3_radius, dodecaprism3_height, dodecaprism3_top_radius,
                                       dodecaprism3_cuboid_length, dodecaprism3_cuboid_height)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of Dodecagonal Prism with Draft", zlim=1)
    # Uncomment the following line if needed for further processing
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
