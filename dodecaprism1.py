import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, dodecaprism1_radius, dodecaprism1_height
from plot import plot_surface
from skimage.draw import polygon  # Requires scikit-image library

def construct_dodecaprism1(scaling, px, centre, radius, prism_height):
    heightmap = np.zeros((px,px))

    #Calculate the dodecagon vertices in [px]
    angles = np.linspace(0, 2*np.pi, 13)[:-1]  # 12 angles for a dodecagon (0 to 2*pi, but exclude last to avoid duplication)
    x_vertex = centre + radius*np.cos(angles)
    y_vertex = centre + radius*np.sin(angles)

    #Convert vertices to pixel grid indices
    x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
    y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

    #Polygon of dodecagon
    rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))

    #Update heightmap
    heightmap[rr, cc] = prism_height
    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
    heightmap = construct_dodecaprism1(scaling, px,centre, dodecaprism1_radius,dodecaprism1_height)
    plot_surface(X_mm, Y_mm, heightmap, "dodecaprism1", zlim=1)
    # Uncomment the following line if needed for further processing
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
