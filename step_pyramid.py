import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm
from plot import plot_surface

#Constants
slope = 1.33 # slope (53.13deg)

#Dimensions of each of the truncated pyramid layers:
pyramids = [
    #First base:
    {"base_size_mm":20, "height_mm":2},
    #Second base:
    {"base_size_mm":10, "height_mm":1},
    #Third pyramid
    {"base_size_mm":5, "height_mm":0.5},
]

#Truncated Pyramid Function:
def construct_steppyramid1(base_size_mm, height_mm, centre, slope, scaling, px, current_height):
    base_size_px = int(base_size_mm * scaling)
    top_size_mm = base_size_mm - 2 * (height_mm / slope)
    top_size_px = int(top_size_mm * scaling)
    
    # Initialise heightmap
    Z = np.zeros((px, px))
    #Centeriing
    for y in range(centre - base_size_px // 2, centre + base_size_px // 2):
        for x in range(centre - base_size_px // 2, centre + base_size_px // 2):
            dist_from_centre = max(abs(x - centre), abs(y - centre))
            if dist_from_centre <= top_size_px // 2:
                Z[y, x] = current_height + height_mm  # Top of the pyramid
            elif dist_from_centre <= base_size_px // 2:
                #Set sloped heights
                Z[y, x] = current_height + height_mm * (1 - (dist_from_centre - top_size_px // 2) / (base_size_px // 2 - top_size_px // 2))
    return Z

#Initialise heightmap for all three truncateds combined
Z_combined = np.zeros((px, px))

#Img mapping dimensions
X = np.linspace(0, px, px)
Y = np.linspace(0, px, px)
X_mm, Y_mm = np.meshgrid(X / scaling, Y / scaling)

#Stack pyramids:
current_height = 0
for pyramid in pyramids:
    Z_pyramid = construct_steppyramid1(pyramid["base_size_mm"], pyramid["height_mm"], centre, slope, scaling, px, current_height)
    Z_combined = np.maximum(Z_combined, Z_pyramid)  #Add new truncation to the data
    current_height += pyramid["height_mm"]  #Vertically shift it

#Normalise:
Z_combined = Z_combined/np.max(Z_combined)
stepPyramidHeightmap = Z_combined

# if __name__ == "__main__":
#     stepPyramidHeightmap = Z_combined
#     stepPyramidTrainingData = step_pyramid_gtb
if __name__ == "__main__":
    heightmap = construct_steppyramid1(20, 2, centre, slope, scaling, px, current_height)
    plot_surface(X_mm, Y_mm, heightmap, "3D Surface pyramidrow4", zlim=1)
    # step_pyramid_gtb = np.expand_dims(heightmap, axis=0)  # gtb heightmap becomes (1, 128, 128)
