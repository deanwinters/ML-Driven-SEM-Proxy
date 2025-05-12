import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, pentaprism2_radius, pentaprism2_height, pentaprism2_angle
from plot import plot_surface
from skimage.draw import polygon 

def construct_pentaprism2(scaling,px, centre, base_radius, prism_height, draft_angle):
    heightmap = np.zeros((px,px))

    #Draft
    tan_draft = np.tan(np.radians(draft_angle))

    #Layers form height
    num_layers = int(prism_height) 
    height_step = prism_height/num_layers

 
    for layer in range(num_layers):
        # Radius due to draft
        current_height = layer*height_step
        current_radius = base_radius - (current_height*tan_draft)

        #Vertices
        angles = np.linspace(0, 2*np.pi, 6)[:-1]
        vertices_x = centre + current_radius*np.cos(angles)
        vertices_y = centre + current_radius*np.sin(angles)

        vertices_x = np.clip(vertices_x, 0, px-1).astype(int)
        vertices_y = np.clip(vertices_y, 0, px-1).astype(int)

        #Polygon generation for n layer
        rr, cc = polygon(vertices_x, vertices_y, shape=(px,px))
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_pentaprism2(scaling,px,centre, pentaprism2_radius,pentaprism2_height, pentaprism2_angle)
    plot_surface(X_mm, Y_mm, heightmap, "pentaprism2", zlim=1)

    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
