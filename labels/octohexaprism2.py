import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, octohexaprism2_hex_radius, octohexaprism2_hex_height,octohexaprism2_oct_radius, octohexaprism2_oct_height,octohexaprism2_draft_angle
from plot import plot_surface

def construct_octohexaprism2(scaling,px,centre, hex_radius, hex_height,oct_radius, oct_height, angle):
    heightmap = np.zeros((px,px))
    
    #Draft angle in radians
    draft_radians = np.radians(angle)
    
    #Calculate vertices ... maybe make this a standalone function insstead of probably repeating it for each heightmap?
    def polygon_vertices(radius, num_sides, center):
        return [
            (center[0] + radius*np.cos(2*np.pi*i / num_sides),
             center[1] + radius*np.sin(2*np.pi*i / num_sides))
            for i in range(num_sides)
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
                            xint = (y-p1y) * (p2x-p1x) / (p2y-p1y) + p1x
                        if p1x == p2x or x <= xint:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    #Draw the drafted octagon layer by layer
    for layer in range(int(oct_height)):
        # Caculate the radius at the current layer height
        layer_radius = oct_radius - layer*np.tan(draft_radians)
        # if layer_radius <= 0: #troubleshooting
        #     break 
        octagon_verts = polygon_vertices(layer_radius, 8, (centre,centre))

        #Set each point within the octogon polygon() for n layers
        for x in range(px):
            for y in range(px):
                if polygon(x, y, octagon_verts):
                    heightmap[y,x] = layer + 1 

    #Draw the drafted hexagon layer by layer on top of the octagon
    base_hex_height = int(oct_height) #initial height
    for layer in range(int(hex_height)):
        #Get the radius at the current layer height
        layer_radius = hex_radius - layer*np.tan(draft_radians)
        # if layer_radius <= 0: # troubleshooting
        #     break
        hexagon_verts = polygon_vertices(layer_radius, 6, (centre, centre))
        
        #Set each point within the hexagon polygon() for n layers
        for x in range(px):
            for y in range(px):
                if polygon(x, y, hexagon_verts):
                    heightmap[y,x] = base_hex_height + layer + 1  

    heightmap = heightmap/np.max(heightmap)

    return heightmap

if __name__ == "__main__":
    heightmap = construct_octohexaprism2(scaling,px,centre,octohexaprism2_hex_radius, octohexaprism2_hex_height,
                                        octohexaprism2_oct_radius, octohexaprism2_oct_height,
                                        octohexaprism2_draft_angle)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of octohexaprism2", zlim=1)