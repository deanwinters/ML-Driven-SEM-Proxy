# Root import (for one level ./subfolders/ project structure)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, tower3_radius, tower3_height, tower3_draft_angle,tower3_cuboid_length,tower3_cuboid1_height,tower3_cuboid2_height,tower3_cuboid3_height,tower3_cuboid4_height
from plot import plot_surface

def construct_tower3(scaling,px,centre,radius,height,draft_angle,cuboid_length,
                     cuboid1_height,cuboid2_height,cuboid3_height,cuboid4_height):

    heightmap = np.zeros((px,px))
    
    #Draft angle in radians
    draft_radians = np.radians(draft_angle)
    
    #Layer generation
    for layer in range(height):
        #Draft inward
        current_radius = radius - layer*np.tan(draft_radians)
        
        #Layers of octogan vertices
        vertices = [
            (centre + current_radius * np.cos(2*np.pi * i/8),
             centre + current_radius * np.sin(2*np.pi * i/8))
            for i in range(8)
        ]
        
        #Check if point is inside polygon (same use as octohexaprism1.py)
        def polygon(x, y, vertices):
            num_vertices = len(vertices)
            inside = False
            p1x, p1y = vertices[0]
            for i in range(num_vertices+1):
                p2x, p2y = vertices[i%num_vertices]
                if y > min(p1y, p2y):
                    if y <= max(p1y, p2y):
                        if x <= max(p1x, p2x):
                            if p1y != p2y:
                                xint = (y-p1y)*(p2x-p1x) / (p2y-p1y) + p1x
                            if p1x == p2x or x <= xint:
                                inside = not inside
                p1x, p1y = p2x, p2y
            return inside

        #Set heights for n layers
        for x in range(px):
            for y in range(px):
                if polygon(x, y, vertices):
                    heightmap[y,x] = layer + 1
    #Cuboid tops (four square faces, common vertex at centre) 
    #Cuboid1:
    cuboid1_min_y = centre-cuboid_length
    cuboid1_max_y = centre
    cuboid1_min_x = centre -cuboid_length
    cuboid1_max_x = centre
    heightmap[cuboid1_min_y:cuboid1_max_y, cuboid1_min_x:cuboid1_max_x] = height + cuboid1_height

    #Cuboid2:
    cuboid2_min_y = centre-cuboid_length
    cuboid2_max_y = centre
    cuboid2_min_x = centre
    cuboid2_max_x = centre+cuboid_length
    heightmap[cuboid2_min_y:cuboid2_max_y, cuboid2_min_x:cuboid2_max_x] = height + cuboid2_height

    #Cuboid3:
    cuboid3_min_y = centre
    cuboid3_max_y = centre+cuboid_length
    cuboid3_min_x = centre
    cuboid3_max_x = centre+cuboid_length
    heightmap[cuboid3_min_y:cuboid3_max_y, cuboid3_min_x:cuboid3_max_x] = height + cuboid3_height

    #Cuboid4:
    cuboid4_min_y = centre
    cuboid4_max_y = centre + cuboid_length
    cuboid4_min_x = centre -cuboid_length
    cuboid4_max_x = centre
    heightmap[cuboid4_min_y:cuboid4_max_y, cuboid4_min_x:cuboid4_max_x] = height + cuboid4_height

    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":
    heightmap = construct_tower3(scaling,px,centre,tower3_radius, tower3_height, tower3_draft_angle,
                                tower3_cuboid_length,
                                tower3_cuboid1_height,tower3_cuboid2_height,tower3_cuboid3_height,tower3_cuboid4_height)
    plot_surface(X_mm, Y_mm, heightmap, "tower3", zlim=1)