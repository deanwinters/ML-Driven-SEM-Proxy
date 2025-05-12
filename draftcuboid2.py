import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, draftcuboid2_base_length, draftcuboid2_base_width, draftcuboid2_height, draftcuboid2_angle,draftcuboid2_cylinder_radius, draftcuboid2_cylinder_height
from plot import plot_surface

def construct_draftcuboid2(scaling, px, centre, base_length, base_width, height, draft_angle, cylinder_radius, cylinder_height):
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

    #Define final heights
    cylinder_radius_px = int(cylinder_radius)
    top_cuboid_height = height
    cylinder_top_height = top_cuboid_height+cylinder_height  

    #Build cylinder:
    for i in range(px):
        for j in range(px):
            dx = i-centre
            dy = j-centre
            distance = np.sqrt(dx**2+dy**2)
            #Inside radius:
            if distance <= cylinder_radius_px:
                heightmap[i, j] = cylinder_top_height

    heightmap = heightmap / np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_draftcuboid2(scaling,px,centre, draftcuboid2_base_length, draftcuboid2_base_width, draftcuboid2_height, draftcuboid2_angle,
                                       draftcuboid2_cylinder_radius, draftcuboid2_cylinder_height)
    plot_surface(X_mm, Y_mm, heightmap, "draftcuboid2", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
