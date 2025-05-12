import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, pyramidrow3_base_length,pyramidrow3_base_width, pyramidrow3_base_height, pyramidrow3_pyramid_length, pyramidrow3_angle
from plot import plot_surface
from skimage.draw import polygon

def construct_pyramidrow3(scaling, px, centre, base_length, base_width, base_height, pyramid_base, draft_angle):
    heightmap = np.zeros((px,px))

    #Cuboid half lengths
    half_length = int(base_length/2)
    half_width = int(base_width/2)

    #cuboid dims
    x_start = max(centre - half_length, 0)
    x_end = min(centre + half_length, px)
    y_start = max(centre - half_width, 0)
    y_end = min(centre + half_width, px)

    #Cuboid height
    heightmap[x_start:x_end, y_start:y_end] = base_height

    #pyramid height based on the draft angle
    half_pyramid_base = pyramid_base/2
    pyramid_height = half_pyramid_base / np.tan(np.radians(draft_angle))

    #No of layers for the pyramids
    num_layers = int(pyramid_height)
    layer_step = pyramid_height/num_layers
    base_step = pyramid_base / (2*num_layers)

    #number of rows and columns of pyramids
    rows = int(base_width/pyramid_base)
    cols = int(base_length/pyramid_base)

    #pyramids in a grid on the top face of the cuboid
    for row in range(rows):
        for col in range(cols):
            #individual pyr centre
            pyramid_center_x = x_start + (col+0.5)*pyramid_base
            pyramid_center_y = y_start + (row+0.5)*pyramid_base

            #pyramid layers
            for layer in range(num_layers):
                current_height = base_height + layer*layer_step
                current_base = pyramid_base - 2*layer*base_step

                #layer bounds
                half_current_base = int(current_base/2)
                x_start_layer = max(int(pyramid_center_x - half_current_base), 0)
                x_end_layer = min(int(pyramid_center_x + half_current_base), px)
                y_start_layer = max(int(pyramid_center_y - half_current_base), 0)
                y_end_layer = min(int(pyramid_center_y + half_current_base), px)

                # Set the heightmap values for the current layer
                heightmap[x_start_layer:x_end_layer, y_start_layer:y_end_layer] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
    heightmap = construct_pyramidrow3(scaling, px, centre, pyramidrow3_base_length, pyramidrow3_base_width, pyramidrow3_base_height, pyramidrow3_pyramid_length, pyramidrow3_angle)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of Cuboid with Pyramids", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0) # gtb heightmap becomes (1, 128, 128)
