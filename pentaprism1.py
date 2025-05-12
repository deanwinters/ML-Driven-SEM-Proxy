import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, pentaprism1_radius, pentaprism1_height
from plot import plot_surface

def construct_pentaprism1(scaling, px, centre, pentaprism1_length, pentaprism1_height):
    heightmap = np.zeros((px,px))

    #Five vertices
    vertices = []
    for k in range(5):
        angle = 2*np.pi*k/5
        x = centre + int(pentaprism1_length*np.cos(angle))
        y = centre + int(pentaprism1_length*np.sin(angle))
        vertices.append((x, y))

    #For each pixel
    for i in range(px):
        for j in range(px):
            #Check if each pixel is inside the pentagon
            intersections = 0
            for v in range(5):
                v1_x,v1_y = vertices[v]
                v2_x,v2_y = vertices[(v+1)%5]
                
                #Ray intersection w/ edge of pentagon
                if ((v1_y>j) != (v2_y>j)) and \
                        (i < (v2_x-v1_x) * (j-v1_y) / (v2_y-v1_y) + v1_x):
                    intersections += 1
            
            #If the ray crosses an odd number of edges the point is inside the pentagon
            if intersections%2 == 1:
                heightmap[j,i] = pentaprism1_height #set height

    #Normalise
    heightmap = heightmap/np.max(heightmap)
    
    return heightmap

if __name__ == "__main__":
    z = construct_pentaprism1(scaling,px,centre,pentaprism1_radius, pentaprism1_height)
    plot_surface(X_mm, Y_mm, z, "pentaprism1", zlim=1)