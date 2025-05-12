# FIVE EXP DATA/HEIGHTMAPS EXCLUDED FROM TRAINING FOR GENERATING RESULTS - steppyramid1, torus1, random1, pyramidrow1, hexagon2
# SOME OTHER HEIGHTMAPS CURRENT NOT FUNCTIONAL - NEEDS RE-CREATING

import numpy as np
from variables import *
from preprocess import load_experimental_data, preprocess, augment_data

# 2510 Trial imports
from cone1 import construct_cone1
from hemisphere1 import construct_hemisphere1
from octohexapentaprism1 import construct_octohexapentaprism1
from octohexapentaprism2 import construct_octohexapentaprism2
from octohexaprism1 import construct_octohexaprism1
from octohexaprism2 import construct_octohexaprism2
from pyramid1 import construct_pyramid1
from random1 import construct_random1
#from step_pyramid1 import construct_steppyramid1, plot_surface
from tower3 import construct_tower3
# 1911 Trial imports
from tetrahedron1 import construct_tetrahedron1
from cutcylinder2 import construct_cutcylinder2
from parallelogram1 import construct_parallelogram1
from cutcylinder1 import construct_cutcylinder1
from cutcylinder2 import construct_cutcylinder2
from pyramidrow4 import construct_pyramidrow4
from pyramidrow3 import construct_pyramidrow3  
from pyramidrow2 import construct_pyramidrow2
#from parallelogram3 import construct_parallelogram3
#from torus2 import construct_torus2
#from paralellogram2 import construct_parallelogram2
#from pyramidrow1 import construct_pyramidrow1
from pentaprism2 import construct_pentaprism2
from pentaprism1 import construct_pentaprism1
#from torus3 import construct_torus3
#from straightslot2 import construct_straightslot2
#from torus1 import construct_torus1
from octaprism1 import construct_octaprism1
from octaprism2 import construct_octaprism2
from icositetragon2 import construct_icositetragon2
from dodecaprism3 import construct_dodecaprism3
#from hexagon2 import construct_hexagon2
from hexagon1 import construct_hexagon1
from dodecaprism2 import construct_dodecaprism2
#from step1 import construct_step1


# Import the validation heightmaps:
#2510
cone1_gtb = construct_cone1(scaling,px,centre, cone1_radius, cone1_height)
hemisphere1_gtb = construct_hemisphere1(scaling,px,centre, hemisphere1_cuboid_size, hemisphere1_cuboid_height,hemisphere1_dome_radius)
octohexapentaprism1_gtb = construct_octohexapentaprism1(scaling,px,centre,
                                              octohexapentaprism1_oct_radius, octohexapentaprism1_oct_height,
                                              octohexapentaprism1_hex_radius, octohexapentaprism1_hex_height,
                                              octohexapentaprism1_pent_radius, octohexapentaprism1_pent_height)
octohexapentaprism2_gtb = construct_octohexapentaprism2(scaling,px,centre,
                                              octohexapentaprism2_oct_radius, octohexapentaprism2_oct_height,
                                              octohexapentaprism2_hex_radius, octohexapentaprism2_hex_height,
                                              octohexapentaprism2_pent_radius, octohexapentaprism2_pent_height,
                                              octohexapentaprism2_angle)
octohexaprism1_gtb = construct_octohexaprism1(scaling,px,centre,
                                              octohexaprism1_hex_radius, octohexaprism1_hex_height, 
                                              octohexaprism1_oct_radius, octohexaprism1_oct_height)
octohexaprism2_gtb = construct_octohexaprism2(scaling,px,centre,
                                              octohexaprism2_hex_radius,octohexaprism2_hex_height,
                                              octohexaprism2_oct_radius, octohexaprism2_oct_height,
                                              octohexaprism2_draft_angle)
pyramid1_gtb = construct_pyramid1(scaling,px,centre, pyramid1_base,pyramid1_height)
random1_gtb = construct_random1(scaling,px,centre,
                                random1_length, random1_width, random1_height, random1_angle,
                                random1_cut1_length, random1_cut1_width,
                                random1_cut2_length, random1_cut2_width,
                                random1_tower_length, random1_tower_height)
#steppyramid1_gtb = construct_steppyramid1(scaling,px,centre,steppyramid1_pyramids, steppyramid1_slope)
tower3_gtb = construct_tower3(scaling,px,centre,
                              tower3_radius, tower3_height, tower3_draft_angle,
                              tower3_cuboid_length,
                              tower3_cuboid1_height,tower3_cuboid2_height,tower3_cuboid3_height, tower3_cuboid4_height)
#1911
tetrahedron1_gtb = construct_tetrahedron1(scaling, px, centre, tetrahedron1_length, tetrahedron1_height, tetrahedron1_angle)
cylinder2_gtb = construct_cutcylinder2(scaling, px, centre, cutcylinder2_radius, cutcylinder2_height)
#parallelogram1_gtb = construct_parallelogram1(scaling, px, centre, parallelogram1_length, parallelogram1_height, parallelogram1_angle)
cutcylinder1_gtb = construct_cutcylinder1(scaling, px, centre, cutcylinder1_radius, cutcylinder1_height)
cutcylinder2_gtb = construct_cutcylinder2(scaling, px, centre, cutcylinder2_radius, cutcylinder2_height)
pyramidrow4_gtb = construct_pyramidrow4(scaling, px, centre, pyramidrow4_board_length, pyramidrow4_board_width,
                                        pyramidrow4_board_height, pyramidrow4_pyramid_length, pyramidrow4_angle)
pyramidrow3_gtb = construct_pyramidrow3(scaling, px, centre, pyramidrow3_base_length, pyramidrow3_base_width, pyramidrow3_base_height,
                                        pyramidrow3_pyramid_length, pyramidrow3_angle)
pyramidrow2_gtb = construct_pyramidrow2(scaling, px, centre, 
                                        pyramidrow2_board_length, pyramidrow2_board_width, pyramidrow2_board_height, 
                                        pyramidrow2_pyramid_base, pyramidrow2_angle)
#parallelogram3_gtb = construct_parallelogram3
#torus2_gtb = construct_torus2
#parallelogram2_gtb = construct_parallelogram2
#pyramidrow1_gtb = construct_pyramidrow1(scaling,px,centre,
#                                        pyramidrow1_board_length, pyramidrow1_board_width, pyramidrow1_board_height,
#                                        pyramidrow1_pyramid_base, pyramidrow1_angle)
pentaprism2_gtb = construct_pentaprism2(scaling,px,centre, pentaprism2_radius, pentaprism2_height, pentaprism2_angle)
pentaprism1_gtb = construct_pentaprism1(scaling,px,centre, pentaprism1_radius, pentaprism1_height)
#torus3_gtb = construct_torus3
#straightslot2_gtb = construct_straightslot2
#torus1_gtb = construct_torus1
octaprism1_gtb = construct_octaprism1(scaling, px, centre, octaprism1_radius, octaprism1_height)
octaprism2_gtb = construct_octaprism2(scaling, px, centre, octaprism2_radius, octaprism2_height, octaprism2_angle)
icositetragon2_gtb = construct_icositetragon2(scaling, px, centre, icositetragon2_base_radius, icositetragon2_height, icositetragon2_angle)
dodecaprism3_gtb = construct_dodecaprism3(scaling, px, centre, 
                                          dodecaprism3_radius, dodecaprism3_height, dodecaprism3_top_radius, 
                                          dodecaprism3_cuboid_length, dodecaprism3_cuboid_height)
#hexagon2_gtb = construct_hexagon2(scaling, px, centre, 
#                                  hexagon2_base_radius, hexagon2_height, hexagon2_angle, 
#                                  hexagon2_cylinder_radius, hexagon2_cylinder_height)
hexagon1_gtb = construct_hexagon1(scaling, px, centre, hexagon1_base_radius, hexagon1_height, hexagon1_angle)
dodecaprism2_gtb = construct_dodecaprism2(scaling, px, centre,
                                          dodecaprism2_radius, dodecaprism2_height, dodecaprism2_top_radius)
#step1_gtb = construct_step1

# GTB Heightmap becomes (1, 128, 128):
#2510
cone1_gtb = np.expand_dims(cone1_gtb,axis=0)
hemisphere1_gtb = np.expand_dims(hemisphere1_gtb,axis=0)
octohexapentaprism1_gtb = np.expand_dims(octohexapentaprism1_gtb,axis=0)
octohexapentaprism2_gtb = np.expand_dims(octohexapentaprism2_gtb,axis=0)
octohexaprism1_gtb = np.expand_dims(octohexaprism1_gtb,axis=0)
octohexaprism2_gtb = np.expand_dims(octohexaprism2_gtb,axis=0)
pyramid1_gtb = np.expand_dims(pyramid1_gtb,axis=0)
random1_gtb = np.expand_dims(random1_gtb,axis=0)
#steppyramid1_gtb = np.expand_dims(steppyramid1_gtb,axis=0)
tower3_gtb = np.expand_dims(tower3_gtb,axis=0)
#1911
tetrahedron1_gtb = np.expand_dims(tetrahedron1_gtb, axis=0)
cylinder2_gtb = np.expand_dims(cylinder2_gtb, axis=0)
#parallelogram1_gtb = np.expand_dims(parallelogram1_gtb, axis=0)
cutcylinder1_gtb = np.expand_dims(cutcylinder1_gtb, axis=0)
cutcylinder2_gtb = np.expand_dims(cutcylinder2_gtb, axis=0)
pyramidrow4_gtb = np.expand_dims(pyramidrow4_gtb, axis=0)
pyramidrow3_gtb = np.expand_dims(pyramidrow3_gtb, axis=0)
pyramidrow2_gtb = np.expand_dims(pyramidrow2_gtb, axis=0)
#parallelogram3_gtb = np.expand_dims(parallelogram3_gtb, axis=0)
#torus2_gtb = np.expand_dims(torus2_gtb, axis=0)
#parallelogram2_gtb = np.expand_dims(parallelogram2_gtb, axis=0)
#pyramidrow1_gtb = np.expand_dims(pyramidrow1_gtb, axis=0)
pentaprism2_gtb = np.expand_dims(pentaprism2_gtb, axis=0)
pentaprism1_gtb = np.expand_dims(pentaprism1_gtb, axis=0)
#torus3_gtb = np.expand_dims(torus3_gtb, axis=0)
#straightslot2_gtb = np.expand_dims(straightslot2_gtb, axis=0)
#torus1_gtb = np.expand_dims(torus1_gtb, axis=0)
octaprism1_gtb = np.expand_dims(octaprism1_gtb, axis=0)
octaprism2_gtb = np.expand_dims(octaprism2_gtb, axis=0)
icositetragon2_gtb = np.expand_dims(icositetragon2_gtb, axis=0)
dodecaprism3_gtb = np.expand_dims(dodecaprism3_gtb, axis=0)
#hexagon2_gtb = np.expand_dims(hexagon2_gtb, axis=0)
hexagon1_gtb = np.expand_dims(hexagon1_gtb, axis=0)
dodecaprism2_gtb = np.expand_dims(dodecaprism2_gtb, axis=0)
#step1_gtb = np.expand_dims(step1_gtb, axis=0)

#Import the experimental data:

trial_date_2510 = "2510"
trial_path_2510 = f"C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/{trial_date_2510}_trial"

trial_date_1911 = "1911"
trial_path_1911 = f"C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/{trial_date_1911}_trial"

#2510
cone1_path = f"{trial_path_2510}/cone1_{trial_date_2510}"
hemisphere1_path = f"{trial_path_2510}/hemisphere1_{trial_date_2510}"
octohexapentaprism1_path = f"{trial_path_2510}/octohexapentaprism1_{trial_date_2510}"
octohexapentaprism2_path = f"{trial_path_2510}/octohexapentaprism2_{trial_date_2510}"
octohexaprism1_path = f"{trial_path_2510}/octohexaprism1_{trial_date_2510}"
octohexaprism2_path = f"{trial_path_2510}/octohexaprism2_{trial_date_2510}"
pyramid1_path = f"{trial_path_2510}/pyramid1_{trial_date_2510}"
random1_path = f"{trial_path_2510}/random1_{trial_date_2510}"
#steppyramid1_path = f"{trial_path_2510}/steppyramid1_{trial_date_2510}"
tower3_path = f"{trial_path_2510}/tower3_{trial_date_2510}"
#1911
tetrahedron1_path = f"{trial_path_1911}/tetrahedron1_{trial_date_1911}"
cylinder2_path = f"{trial_path_1911}/cylinder2_{trial_date_1911}"
#parallelogram1_path = f"{trial_path_1911}/parallelogram1_{trial_date_1911}"
cutcylinder1_path = f"{trial_path_1911}/cutcylinder1_{trial_date_1911}"
cutcylinder2_path = f"{trial_path_1911}/cutcylinder2_{trial_date_1911}"
pyramidrow4_path = f"{trial_path_1911}/pyramidrow4_{trial_date_1911}"
pyramidrow3_path = f"{trial_path_1911}/pyramidrow3_{trial_date_1911}"
pyramidrow2_path = f"{trial_path_1911}/pyramidrow2_{trial_date_1911}"
#parallelogram3_path = f"{trial_path_1911}/parallelogram3_{trial_date_1911}"
#torus2_path = f"{trial_path_1911}/torus2_{trial_date_1911}"
#parallelogram2_path = f"{trial_path_1911}/parallelogram2_{trial_date_1911}"
#pyramidrow1_path = f"{trial_path_1911}/pyramidrow1_{trial_date_1911}"
pentaprism2_path = f"{trial_path_1911}/pentaprism2_{trial_date_1911}"
pentaprism1_path = f"{trial_path_1911}/pentaprism1_{trial_date_1911}"
#torus3_path = f"{trial_path_1911}/torus3_{trial_date_1911}"
#straightslot2_path = f"{trial_path_1911}/straightslot2_{trial_date_1911}"
#torus1_path = f"{trial_path_1911}/torus1_{trial_date_1911}"
octaprism1_path = f"{trial_path_1911}/octaprism1_{trial_date_1911}"
octaprism2_path = f"{trial_path_1911}/octaprism2_{trial_date_1911}"
icositetragon2_path = f"{trial_path_1911}/icositetragon2_{trial_date_1911}"
dodecaprism3_path = f"{trial_path_1911}/dodecaprism3_{trial_date_1911}"
#hexagon2_path = f"{trial_path_1911}/hexagon2_{trial_date_1911}"
hexagon1_path = f"{trial_path_1911}/hexagon1_{trial_date_1911}"
dodecaprism2_path = f"{trial_path_1911}/dodecaprism2_{trial_date_1911}"
#step1_path = f"{trial_path_1911}/step1_{trial_date_1911}"

#Preprocess experimental data:
#2510
raw_cone1, cone1 = preprocess(px, gallery=load_experimental_data(cone1_path))
raw_hemisphere1, hemisphere1 = preprocess(px, gallery=load_experimental_data(hemisphere1_path))
raw_octohexapentaprism1, octohexapentaprism1 = preprocess(px, gallery=load_experimental_data(octohexapentaprism1_path))
raw_octohexapentaprism2, octohexapentaprism2 = preprocess(px, gallery=load_experimental_data(octohexapentaprism2_path))
raw_octohexaprism1, octohexaprism1 = preprocess(px, gallery=load_experimental_data(octohexaprism1_path))
raw_octohexaprism2, octohexaprism2 = preprocess(px, gallery=load_experimental_data(octohexaprism2_path))
raw_pyramid1, pyramid1 = preprocess(px, gallery=load_experimental_data(pyramid1_path))
raw_random1, random1 = preprocess(px, gallery=load_experimental_data(random1_path))
#raw_steppyramid1, steppyramid1 = preprocess(px, gallery=load_experimental_data(steppyramid1_path))
raw_tower3, tower3 = preprocess(px, gallery=load_experimental_data(tower3_path))
#1911
raw_tetrahedron1, tetrahedron1 = preprocess(px, gallery=load_experimental_data(tetrahedron1_path))
raw_cylinder2, cylinder2 = preprocess(px, gallery=load_experimental_data(cylinder2_path))
#raw_parallelogram1, parallelogram1 = preprocess(px, gallery=load_experimental_data(parallelogram1_path))
raw_cutcylinder1, cutcylinder1 = preprocess(px, gallery=load_experimental_data(cutcylinder1_path))
raw_cutcylinder2, cutcylinder2 = preprocess(px, gallery=load_experimental_data(cutcylinder2_path))
raw_pyramidrow4, pyramidrow4 = preprocess(px, gallery=load_experimental_data(pyramidrow4_path))
raw_pyramidrow3, pyramidrow3 = preprocess(px, gallery=load_experimental_data(pyramidrow3_path))
raw_pyramidrow2, pyramidrow2 = preprocess(px, gallery=load_experimental_data(pyramidrow2_path))
#raw_parallelogram3, parallelogram3 = preprocess(px, gallery=load_experimental_data(parallelogram3_path))
#raw_torus2, torus2 = preprocess(px, gallery=load_experimental_data(torus2_path))
#raw_parallelogram2, parallelogram2 = preprocess(px, gallery=load_experimental_data(parallelogram2_path))
#raw_pyramidrow1, pyramidrow1 = preprocess(px, gallery=load_experimental_data(pyramidrow1_path))
raw_pentaprism2, pentaprism2 = preprocess(px, gallery=load_experimental_data(pentaprism2_path))
raw_pentaprism1, pentaprism1 = preprocess(px, gallery=load_experimental_data(pentaprism1_path))
#raw_torus3, torus3 = preprocess(px, gallery=load_experimental_data(torus3_path))
#raw_straightslot2, straightslot2 = preprocess(px, gallery=load_experimental_data(straightslot2_path))
#raw_torus1, torus1 = preprocess(px, gallery=load_experimental_data(torus1_path))
raw_octaprism1, octaprism1 = preprocess(px, gallery=load_experimental_data(octaprism1_path))
raw_octaprism2, octaprism2 = preprocess(px, gallery=load_experimental_data(octaprism2_path))
raw_icositetragon2, icositetragon2 = preprocess(px, gallery=load_experimental_data(icositetragon2_path))
raw_dodecaprism3, dodecaprism3 = preprocess(px, gallery=load_experimental_data(dodecaprism3_path))
#raw_hexagon2, hexagon2 = preprocess(px, gallery=load_experimental_data(hexagon2_path))
raw_hexagon1, hexagon1 = preprocess(px, gallery=load_experimental_data(hexagon1_path))
raw_dodecaprism2, dodecaprism2 = preprocess(px, gallery=load_experimental_data(dodecaprism2_path))
#raw_step1, step1 = preprocess(px, gallery=load_experimental_data(step1_path))


#Combine the datasets by concatenating images and labels along the batch axis

combined_data = np.concatenate([
    cone1, hemisphere1, octohexapentaprism1, octohexapentaprism2, octohexaprism1, octohexaprism2, 
    pyramid1, tower3, tetrahedron1, cylinder2, cutcylinder1, 
    cutcylinder2, pyramidrow4, pyramidrow3, pyramidrow2, pentaprism2, pentaprism1,
    octaprism1, octaprism2, icositetragon2, dodecaprism3, hexagon1, dodecaprism2
], axis=0)

combined_gtb = np.concatenate([
    cone1_gtb, hemisphere1_gtb, octohexapentaprism1_gtb, octohexapentaprism2_gtb, octohexaprism1_gtb, octohexaprism2_gtb, 
    pyramid1_gtb, tower3_gtb, tetrahedron1_gtb, cylinder2_gtb, cutcylinder1_gtb, 
    cutcylinder2_gtb, pyramidrow4_gtb, pyramidrow3_gtb, pyramidrow2_gtb,
    pentaprism2_gtb, pentaprism1_gtb, 
    octaprism1_gtb, octaprism2_gtb, icositetragon2_gtb, dodecaprism3_gtb, hexagon1_gtb, dodecaprism2_gtb
])

#Number of individual objects used:
print("Number of training objects, heightmaps:")
print(len(combined_data), len(combined_gtb))
#Tracking data dimensionality:
print("BEFORE ROTATION:")
print("Training input shape: ",np.shape(combined_data))
print("Training validation shape: ",np.shape(combined_gtb))

#Augmentation:
 
angles = [i*1 for i in range(25)] #rotation angles

#Rotate the data to make augmented sets
augcombined_data, augcombined_gtb = augment_data(combined_data, combined_gtb, angles)

#Concatenate original data with augmented data
combined_data = np.concatenate([combined_data, augcombined_data], axis=0)
combined_gtb = np.concatenate([combined_gtb, augcombined_gtb], axis=0)

#Shuffle the augmented dataset
shuffle = np.random.permutation(combined_data.shape[0])
combined_data = combined_data[shuffle]
combined_gtb = combined_gtb[shuffle]

#Tracking data dimensionality:
print("AFTER ROTATION:")
print("Training input shape: ", np.shape(combined_data))
print("Training validation shape: ", np.shape(combined_gtb))
