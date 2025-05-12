import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, octohexapentaprism1_oct_radius, octohexapentaprism1_oct_height,octohexapentaprism1_hex_radius, octohexapentaprism1_hex_height, octohexapentaprism1_pent_radius, octohexapentaprism1_pent_height
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_octohexapentaprism1(scaling,px, centre, oct_radius, oct_height, hex_radius, hex_height, pent_radius, pent_height):
    heightmap = np.zeros((px,px))

    #Starting stacking pos
    current_base_height = 0

    #Helper function to construct a polygonal prism layer
    def add_prism_layer(radius, num_sides, height, base_height):
        #Number of layers from height
        num_layers = int(height)
        height_step = height/num_layers

        #Vertices for n-polygon
        angles = np.linspace(0, 2*np.pi, num_sides+1)[:-1]

        #Build ecah layer of the prism
        for layer in range(num_layers):
            current_height = base_height + layer*height_step

            #Create vertices
            x_vertex = centre + radius*np.cos(angles)
            y_vertex = centre + radius*np.sin(angles)

            x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
            y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

            #Polygon layer
            rr, cc = polygon(x_vertex, y_vertex, shape=(px, px))
            
            #Set height
            heightmap[rr,cc] = current_height

        return base_height + height

    #Octogonal prism
    current_base_height = add_prism_layer(oct_radius, 8, oct_height, current_base_height)

    #Hexagonal prism on top
    current_base_height = add_prism_layer(hex_radius, 6, hex_height, current_base_height)

    #Pentagonal prism on top again
    current_base_height = add_prism_layer(pent_radius, 5, pent_height, current_base_height)

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_octohexapentaprism1(scaling,px,centre,
                                              octohexapentaprism1_oct_radius, octohexapentaprism1_oct_height,
                                              octohexapentaprism1_hex_radius, octohexapentaprism1_hex_height,
                                              octohexapentaprism1_pent_radius, octohexapentaprism1_pent_height)
    plot_surface(X_mm, Y_mm, heightmap, "octohexapentaprism1", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
