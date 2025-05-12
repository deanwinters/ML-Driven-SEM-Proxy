import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm,  octaprism1_radius, octaprism1_height
from plot import plot_surface
from skimage.draw import polygon

def construct_octaprism1(scaling,px, centre, radius, prism_height):
    heightmap = np.zeros((px,px))

    #Layers form height
    num_layers = int(prism_height) 
    height_step = prism_height/num_layers

    #Octagonal vertices
    angles = np.linspace(0, 2*np.pi, 9)[:-1]
    x_vertex = centre + radius*np.cos(angles)
    y_vertex = centre + radius*np.sin(angles)

    x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
    y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

    #Polygon layer
    rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))

    #Set height
    for layer in range(num_layers):
        current_height = layer*height_step
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_octaprism1(scaling, px, centre, octaprism1_radius, octaprism1_height)
    plot_surface(X_mm, Y_mm, heightmap, "octoprism1", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
