import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, icositetragon2_height, icositetragon2_height, icositetragon2_angle
from plot import plot_surface
from skimage.draw import polygon
import numpy as np

def construct_icositetragon2(scaling,px, centre, base_radius, prism_height, draft_angle):
    heightmap = np.zeros((px,px))

    #Deaft
    tan_draft = np.tan(np.radians(draft_angle))
    
    #Height layers
    num_layers = int(prism_height)
    height_step = prism_height/num_layers

    #Set radius for each layer
    for layer in range(num_layers):
        current_height = layer*height_step
        current_radius = base_radius - current_height*tan_draft

        #Vertices at this radius
        angles = np.linspace(0, 2*np.pi, 25)[:-1]  # 6 for hexagon
        x_vertex = centre + current_radius*np.cos(angles)
        y_vertex = centre + current_radius*np.sin(angles)

        x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
        y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

        #Polygon mask for each layer
        rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
        
        #Set height insdie the icositetragon for current layer
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_icositetragon2(scaling,px, centre, icositetragon2_height, icositetragon2_height, icositetragon2_angle)
    plot_surface(X_mm, Y_mm, heightmap, "icositetragon2", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
