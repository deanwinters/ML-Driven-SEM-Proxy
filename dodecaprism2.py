import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, dodecaprism2_radius, dodecaprism2_height, dodecaprism2_top_radius
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_dodecaprism2(scaling,px, centre, base_radius, height, top_radius):
    heightmap = np.zeros((px, px))
    
    #split into layers
    num_layers = int(height)
    height_step = height/num_layers

    for layer in range(num_layers):
        #Height for layer
        current_height = layer*height_step
        #associated radius
        current_radius = base_radius + (top_radius-base_radius)*(current_height/height)

        #Calculate vertices for the dodecagon at layer
        angles = np.linspace(0, 2*np.pi, 13)[:-1]  # 12 angles for dodecagon
        vertices_x = centre + current_radius*np.cos(angles)
        vertices_y = centre + current_radius*np.sin(angles)

        #Convert vertices to pixel grid indices
        vertices_x = np.clip(vertices_x, 0, px-1).astype(int)
        vertices_y = np.clip(vertices_y, 0, px-1).astype(int)

        #Layered polygon of dodecagon
        rr, cc = polygon(vertices_x, vertices_y, shape=(px,px))
        
        #Update heightmap
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":
    # Use parameters from external sources
    heightmap = construct_dodecaprism2(scaling, px, centre, dodecaprism2_radius, dodecaprism2_height, dodecaprism2_top_radius)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of Dodecagonal Prism with Draft", zlim=1)
    # Uncomment the following line if needed for further processing
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
