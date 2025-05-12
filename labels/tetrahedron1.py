import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, tetrahedron1_length, tetrahedron1_height, tetrahedron1_angle
from plot import plot_surface
from skimage.draw import polygon

def rotate_point(x, y, center_x, center_y, angle_deg):
    angle_rad = np.radians(angle_deg)
    new_x = np.cos(angle_rad)*(x-center_x) - np.sin(angle_rad)*(y-center_y) + center_x
    new_y = np.sin(angle_rad)*(x-center_x) + np.cos(angle_rad)*(y-center_y) + center_y
    return new_x, new_y

def construct_tetrahedron1(scaling,px, centre, base_length, shape_height, draft_angle):

    heightmap = np.zeros((px,px))

    #Calculate the vertices at the base
    half_base = base_length/2
    tan_draft = np.tan(np.radians(draft_angle))

    #No of layers
    num_layers = int(shape_height)
    height_step = shape_height/num_layers
    base_step = half_base/num_layers

    #vertices for the base triangle (before rot.)
    #Rotation done to match experimental data orientation
    vertices_base = np.array([
        [centre, centre-half_base], #top
        [centre-half_base, centre+half_base], #bottom left
        [centre+half_base, centre+half_base] #bottom right
    ])

    # Layer construction
    for layer in range(num_layers):
        current_height = layer*height_step
        current_base_reduction = layer*base_step

        #Adjust the vertices with the current base reduction
        vertices_x = [
            centre, 
            centre - (half_base - current_base_reduction),
            centre + (half_base - current_base_reduction)
        ]
        vertices_y = [
            centre - (half_base - current_base_reduction),
            centre + (half_base - current_base_reduction),
            centre + (half_base - current_base_reduction)
        ]

        #Rotate vertices by 90 degrees clockwise (EXPERIMENTAL DATA ORIENTATION)
        vertices_rotated_x, vertices_rotated_y = zip(
            *[rotate_point(x, y, centre, centre, 90) for x, y in zip(vertices_x,vertices_y)]
        )

        #Convert vertices to pixel
        vertices_rotated_x = np.clip(vertices_rotated_x, 0, px-1).astype(int)
        vertices_rotated_y = np.clip(vertices_rotated_y, 0, px-1).astype(int)

        #Polygon layer gen.
        rr, cc = polygon(vertices_rotated_x, vertices_rotated_y, shape=(px,px))
        
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
    # Create heightmap for the rotated tetrahedral-like shape
    heightmap = construct_tetrahedron1(scaling,px, centre, tetrahedron1_length, tetrahedron1_height, tetrahedron1_angle)
    plot_surface(X_mm, Y_mm, heightmap, "Tetrahedron1", zlim=1)
    # Uncomment the following line if needed for further processing
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
