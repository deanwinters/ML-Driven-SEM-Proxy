import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, draftcuboid1_base_length, draftcuboid1_base_width, draftcuboid1_height, draftcuboid1_angle
from plot import plot_surface

def construct_draftcuboid1(scaling, px, centre, base_length, base_width, height, draft_angle):
    heightmap = np.zeros((px, px))

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

    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":

    heightmap = construct_draftcuboid1(scaling,px,centre, draftcuboid1_base_length, draftcuboid1_base_width, draftcuboid1_height, draftcuboid1_angle)
    plot_surface(X_mm, Y_mm, heightmap, "draftcuboid1", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
