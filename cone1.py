import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, cone1_radius, cone1_height
from plot import plot_surface

def construct_cone1(scaling,px,centre,radius,height):
    # Empty heightmap
    heightmap = np.zeros((px, px))
    #Iterate each px to map the height
    for i in range(px):
        for j in range(px):
            dx = i-centre
            dy = j-centre
            distance_from_center = np.sqrt(dx**2 + dy**2)
            
            #For inside the base:
            if distance_from_center <= radius:
                #1:1 decrease (45deg)
                heightmap[i,j] = height*(1 - distance_from_center/radius)
    #Normalise
    heightmap = heightmap/np.max(heightmap)
    return heightmap

#Plotting:
if __name__ == "__main__":
    heightmap = construct_cone1(scaling,px,centre,cone1_radius,cone1_height)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of Cone", zlim=1)