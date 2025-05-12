import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm, octohexaprism1_hex_radius, octohexaprism1_hex_height, octohexaprism1_oct_radius, octohexaprism1_oct_height
from plot import plot_surface

def construct_octohexaprism1(scaling,px,centre, hex_radius, hex_height,oct_radius, oct_height):
    heightmap = np.zeros((px,px))

    #Calculate vertices ... maybe make this a standalone function insstead of probably repeating it for each heightmap?
    def polygon_vertices(radius, num_sides, center):
        return [
            (center[0] + radius*np.cos(2*np.pi*i / num_sides),
             center[1] + radius*np.sin(2*np.pi*i / num_sides))
            for i in range(num_sides)
        ]
    hexagon_verts = polygon_vertices(hex_radius, 6, (centre, centre))
    octagon_verts = polygon_vertices(oct_radius, 8, (centre, centre))
    
    #PCheck if point is inside polygon
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
                            xinters = (y-p1y) * (p2x-p1x) / (p2y-p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    #Place hexagon polygon() points
    for i in range(px):
        for j in range(px):
            if polygon(i,j, hexagon_verts):
                heightmap[j,i] += hex_height  # Raise hexagon area by hex_height_px

    #Place octogon polygon() points
    for i in range(px):
        for j in range(px):
            if polygon(i,j, octagon_verts):
                heightmap[j,i] += oct_height  # Raise octagon area by oct_height_px

    heightmap = heightmap/np.max(heightmap)

    return heightmap


if __name__ == "__main__":
    heightmap = construct_octohexaprism1(scaling,px,centre,octohexaprism1_hex_radius, octohexaprism1_hex_height,
                                    octohexaprism1_oct_radius, octohexaprism1_oct_height)

    plot_surface(X_mm, Y_mm, heightmap, "3D Surface of octohexaprism1", zlim=1)