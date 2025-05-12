import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, icositetragon1_base_radius, icositetragon1_height
from plot import plot_surface
from skimage.draw import polygon

def construct_icositetragon1(px, centre, radius, prism_height):
    heightmap = np.zeros((px, px))

    #Number of layers for height
    num_layers = int(prism_height)
    height_step = prism_height/num_layers

    #Define the vertices
    angles = np.linspace(0, 2*np.pi, 25)[:-1]  
    x_vertex = centre + radius*np.cos(angles)
    y_vertex = centre + radius*np.sin(angles)

    x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
    y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

    #Polgyon mask for each layer
    rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))

    #Heigth for each layer
    for layer in range(num_layers):
        current_height = layer*height_step
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
    heightmap = construct_icositetragon1(px, centre, icositetragon1_base_radius, icositetragon1_height)
    plot_surface(X_mm, Y_mm, heightmap, "icositetragon1", zlim=1)
    # Uncomment the following line if needed for further processing
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
