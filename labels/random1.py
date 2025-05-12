import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm,random1_length,random1_width, random1_height, random1_angle,random1_cut1_length, random1_cut1_width,random1_cut2_length, random1_cut2_width,random1_tower_length, random1_tower_height
from plot import plot_surface


def construct_random1(scaling,px,centre,length,width,height,draft_angle,
                      cut1_length,cut1_width,
                      cut2_length,cut2_width,
                      tower_length, tower_height):

    heightmap = np.zeros((px,px))

    #Draft angle in radians
    draft_radians = np.radians(draft_angle)
    
    #Build the shape layer by layer from bottom up
    for layer in range(int(height)):
        #Angular draft
        draft_reduction = layer * np.tan(draft_radians)
        current_length = length - 2*draft_reduction
        current_width = width - 2*draft_reduction
        
        #Rectangular layer bounds
        min_x = int(centre - current_length/2)
        max_x = int(centre + current_length/2)
        min_y = int(centre - current_width/2)
        max_y = int(centre + current_width/2)
              
        #Layer height
        heightmap[min_y:max_y, min_x:max_x] = layer + 1

    #First cut; area enclosed inside the structure
    cut_min_x = int(centre - cut1_length/2)
    cut_max_x = int(centre + cut1_length/2)
    cut_min_y = int(centre - cut1_width/2)
    cut_max_y = int(centre + cut1_width/2)
    heightmap[cut_min_y:cut_max_y, cut_min_x:cut_max_x] = 0

    #Second cut; area is one quadrant of the structure
    second_cut_min_x = int(centre)
    second_cut_max_x = int(centre+cut2_length)
    second_cut_min_y = int(centre)
    second_cut_max_y = int(centre+cut2_width)
    heightmap[second_cut_min_y:second_cut_max_y, second_cut_min_x:second_cut_max_x] = 0

    #Tower part:
    tower_min_x = cut_min_x - int(tower_length)
    tower_max_x = cut_min_x
    tower_min_y = cut_min_y - int(tower_length)
    tower_max_y = cut_min_y
    heightmap[tower_min_y:tower_max_y, tower_min_x:tower_max_x] = height + int(tower_height)

    #Normalise:
    heightmap = heightmap/np.max(heightmap)
    return heightmap

if __name__ == "__main__":
    heightmap = construct_random1(scaling,px,centre,
                                  random1_length,random1_width, random1_height, random1_angle,
                                  random1_cut1_length, random1_cut1_width,
                                  random1_cut2_length, random1_cut2_width,
                                  random1_tower_length, random1_tower_height)
    plot_surface(X_mm, Y_mm, heightmap, "random1", zlim=1)

