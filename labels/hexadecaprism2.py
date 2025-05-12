import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, hexadecaprism2_radius,hexadecaprism2_height,hexadecaprism2_angle
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_hexadecaprism2(scaling, px, centre, base_radius, prism_height, draft_angle):
    heightmap = np.zeros((px,px))

    #Draft
    tan_draft = np.tan(np.radians(draft_angle))
    
    # Number of layers
    num_layers = int(prism_height)
    height_step = prism_height / num_layers

    #Create face at each layer
    for layer in range(num_layers):
        current_height = layer*height_step

        # Calculate the radius at this height due to the draft angle
        current_radius = base_radius - current_height*tan_draft

        #  Hexadecagon vertices
        angles = np.linspace(0, 2*np.pi, 17)[:-1]
        x_vertex = centre + current_radius*np.cos(angles)
        y_vertex = centre + current_radius*np.sin(angles)

        # Convert vertices to pixel grid indices
        x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
        y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

        #Polygon mask for each layer
        rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
        
        # Set the heightmap values inside the hexadecagon for this layer's height
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_hexadecaprism2(scaling, px, centre, hexadecaprism2_radius,hexadecaprism2_height,hexadecaprism2_angle)
    plot_surface(X_mm, Y_mm, heightmap, "hexadecaprism2", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
