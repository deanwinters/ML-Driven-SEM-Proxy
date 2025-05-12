import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, hexagon2_base_radius, hexagon2_height, hexagon2_angle, hexagon2_cylinder_radius,hexagon2_cylinder_height
from plot import plot_surface
from skimage.draw import polygon

def construct_hexagon2(scaling,px, centre, base_radius, prism_height, draft_angle, cylinder_radius, cylinder_height):
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
        angles = np.linspace(0, 2*np.pi, 7)[:-1]  # 6 for hexagon
        x_vertex = centre + current_radius*np.cos(angles)
        y_vertex = centre + current_radius*np.sin(angles)

        x_vertex = np.clip(x_vertex, 0, px-1).astype(int)
        y_vertex = np.clip(y_vertex, 0, px-1).astype(int)

        #Polygon mask for each layer
        rr, cc = polygon(x_vertex, y_vertex, shape=(px,px))
        
        #Set height
        heightmap[rr,cc] = current_height

    #Loop over each pixel to calculate the height
    for i in range(px):
        #Get radial distance from centre
        for j in range(px):
            dx = i-centre
            dy = j-centre
            distance_from_centre = np.sqrt(dx**2+dy**2)
            #Inside radius:
            if distance_from_centre <= cylinder_radius:
                heightmap[i,j] =  prism_height + cylinder_height

    # Normalize the heightmap for consistent plotting
    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":

    heightmap = construct_hexagon2(scaling,px, centre, hexagon2_base_radius, hexagon2_height, hexagon2_angle,
                                   hexagon2_cylinder_radius,hexagon2_cylinder_height)
    plot_surface(X_mm, Y_mm, heightmap, "hexagon2", zlim=2)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
