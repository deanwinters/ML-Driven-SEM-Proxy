import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, hexadecaprism1_radius, hexadecaprism1_height
from plot import plot_surface
from skimage.draw import polygon

def construct_hexadecaprism1(scaling,px, centre, hexadecagon_radius, prism_height):
    heightmap = np.zeros((px,px))

    #Number of layers
    num_layers = int(prism_height)
    height_step = prism_height/num_layers

    #16 hexadecagon vertices
    angles = np.linspace(0, 2*np.pi, 17)[:-1]  # 16 angles for hexadecagon (0 to 2*pi, excluding duplicate 2*pi)
    x_vertex = centre + hexadecagon_radius*np.cos(angles)
    y_vertex = centre + hexadecagon_radius*np.sin(angles)

    # Convert vertices to pixel grid indices
    x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
    y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

    #Polgygon for each layer
    rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))

    # Set height for each layer
    for layer in range(num_layers):
        current_height = layer*height_step
        heightmap[rr,cc] = current_height

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    # Create heightmap for hexadecagonal prism
    heightmap = construct_hexadecaprism1(scaling, px, centre, hexadecaprism1_radius, hexadecaprism1_height)
    plot_surface(X_mm, Y_mm, heightmap, "hexadecaprism1", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
