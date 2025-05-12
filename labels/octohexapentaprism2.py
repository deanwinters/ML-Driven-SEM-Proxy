import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, octohexapentaprism2_oct_radius, octohexapentaprism2_oct_height,octohexapentaprism2_hex_radius, octohexapentaprism2_hex_height, octohexapentaprism2_pent_radius, octohexapentaprism2_pent_height,octohexapentaprism2_angle
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_octohexapentaprism2(scaling, px, centre, oct_radius, oct_height, hex_radius, hex_height, pent_radius, pent_height, draft_angle):
    heightmap = np.zeros((px, px))
    current_base_height = 0

    #Draft
    tan_draft = np.tan(np.radians(draft_angle))

    # Helper function to construct a drafted polygonal prism layer
    def add_prism_layer(base_radius, num_sides, height, base_height):
        #Layers based on top height
        num_layers = int(height)
        height_step = height/num_layers

        # Build layers for the drafted polygonal prism
        for layer in range(num_layers):
            current_height = base_height + layer*height_step

            # Radius due to draft
            current_radius = base_radius - (layer*height_step*tan_draft)

            #Vertices
            angles = np.linspace(0, 2*np.pi, num_sides+1)[:-1]
            x_vertex = centre + current_radius*np.cos(angles)
            y_vertex = centre + current_radius*np.sin(angles)

            x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
            y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

            # Generate a polygonal mask for the current prism layer
            rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
            
            # Set the heightmap values inside the polygon for this layer's height
            heightmap[rr,cc] = current_height

        return base_height + height 

    #Oct block
    current_base_height = add_prism_layer(oct_radius, 8, oct_height, current_base_height)

    #Hex block on top
    current_base_height = add_prism_layer(hex_radius, 6, hex_height, current_base_height)

    #Pent block on top agian
    current_base_height = add_prism_layer(pent_radius, 5, pent_height, current_base_height)

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
 
    heightmap = construct_octohexapentaprism2(scaling,px,centre,
                                              octohexapentaprism2_oct_radius, octohexapentaprism2_oct_height,
                                              octohexapentaprism2_hex_radius, octohexapentaprism2_hex_height,
                                              octohexapentaprism2_pent_radius, octohexapentaprism2_pent_height,
                                              octohexapentaprism2_angle)
    plot_surface(X_mm, Y_mm, heightmap, "octohexapentaprism2", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
