import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, octaprism2_radius, octaprism2_height,octaprism2_angle
from plot import plot_surface
from skimage.draw import polygon

def construct_octaprism2(scaling, px, centre, radius, prism_height, draft_angle):
    heightmap = np.zeros((px,px))

    #Layers from height
    num_layers = int(prism_height)
    height_step = prism_height/num_layers

    #Draft
    tan_draft = np.tan(np.radians(draft_angle))

    #Height and radius set at each layer as drafted
    for layer in range(num_layers):
        current_height = layer*height_step
        current_radius = radius - (current_height*tan_draft)

        #Octogon vertices
        angles = np.linspace(0, 2*np.pi, 9)[:-1]
        x_vertex = centre + current_radius*np.cos(angles)
        y_vertex = centre + current_radius*np.sin(angles)

        x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
        y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

        #Polygon layer
        rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
        
        #Set height
        heightmap[rr,cc] = current_height

    # Normalize the heightmap for plotting consistency
    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
    heightmap = construct_octaprism2(scaling, px, centre, octaprism2_radius, octaprism2_height,octaprism2_angle)
    plot_surface(X_mm, Y_mm, heightmap, "octaprism1", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
