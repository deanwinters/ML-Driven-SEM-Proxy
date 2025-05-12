#train_setup.py currently pulls * from this file

import numpy as np


px = 256 # [px], desired image side dimension
scaling = 8 #[px/mm] resolution
centre = px//2 #image centre for heightmaps, etc.
integrationTime = 2 #[s]

numtest = 125
filepath = f"C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/test_{numtest}"
darkframe_filepath = f"{filepath}_DARKFRAME"

#Img mapping dimensions
X = np.linspace(0, px, px)
Y = np.linspace(0, px, px)
X_mm, Y_mm = np.meshgrid(X/scaling, Y/scaling)


#steppyramid1 parameters
steppyramid1_slope = 1.33 # slope (53.13 deg)
steppyramid1_pyramids = [ #Dimensions of each of the truncated pyramid layers:
    {"base_mm":20, "height_mm":2},
    {"base_mm":10, "height_mm":1},
    {"base_mm":5, "height_mm":0.5},
]

#hemisphere1 parameters
hemisphere1_cuboid_size = 35 *scaling # 35mm x 35mm cuboid base
hemisphere1_dome_radius = 12.5 *scaling # 12.5mm hemisphere radius
hemisphere1_cuboid_height = 10 # mm


#cuboid1 parameters
cuboid1_size = 20 *scaling # 20mm x 20mm face
cuboid1_height = 10 #10mm height


#pyramid1 parameters:
pyramid1_base = 20 *scaling
pyramid1_height = 10*np.sqrt(2) #45deg incline


#cone1 parameters
cone1_radius = 7.5 *scaling
cone1_height = 7.5 

# cylinder1 parameters
cylinder1_radius = 15 *scaling
cylinder1_height = 15

#cylinder2 parameters:
cylinder2_radius = 12 * scaling
cylinder2_height = 12

#prism1 parameters:
prism1_sidelength = 25 *scaling
prism1_height = 15

#octohexaprism1 parameters
octohexaprism1_hex_radius = 10 *scaling/2
octohexaprism1_hex_height = 6/2
octohexaprism1_oct_radius = 12.64 *scaling/2
octohexaprism1_oct_height = 8/2

#octohexaprism2 parameters
octohexaprism2_hex_radius = 10 *scaling/2
octohexaprism2_hex_height = 6/2
octohexaprism2_oct_radius = 12.64 *scaling/2
octohexaprism2_oct_height = 8/2
octohexaprism2_draft_angle = 25

#random1 parameters:
random1_length = 33.53 *scaling/2
random1_width = 28.53 *scaling/2
random1_height = 10  *scaling/2
random1_angle = 10
random1_cut1_length = 20 *scaling/2
random1_cut1_width = 15 *scaling/2
random1_cut2_length = 16.76 *scaling/2
random1_cut2_width = 14.26 *scaling/2
random1_tower_length = 5 *scaling/2
random1_tower_height = 10 *scaling/2

#tower3 parameters:
tower3_radius = 19.547395 *scaling//2
tower3_height = 6//2
tower3_draft_angle = 55 
tower3_cuboid_length = 10 *scaling//2
tower3_cuboid1_height = 16//2
tower3_cuboid2_height = 12//2
tower3_cuboid3_height = 8//2
tower3_cuboid4_height = 4//2

#cutcylinder1 parameters:
cutcylinder1_radius = 6 *scaling
cutcylinder1_height = 8

#cutcylinder2 parameters:
cutcylinder2_radius = 6 *scaling
cutcylinder2_height = 12

#dodecaprism1 parameters:
dodecaprism1_radius = 7.5 *scaling
dodecaprism1_height = 10

#dodecaprism2 parameters:
dodecaprism2_radius = 7.5 *scaling
dodecaprism2_height = 10
dodecaprism2_top_radius = 5.645 *scaling
dodecaprism2_angle = 10

#dodecaprism3 parameters:
dodecaprism3_radius = 7.5 *scaling
dodecaprism3_height = 10
dodecaprism3_top_radius = 5.645 *scaling
dodecaprism3_angle = 10
dodecaprism3_cuboid_length = 3 *scaling
dodecaprism3_cuboid_height = 1

#draftcuboid1 parameters:
draftcuboid1_base_length = 26 *scaling
draftcuboid1_base_width = 21 *scaling
draftcuboid1_height = 8 *scaling
draftcuboid1_angle = 45

#draftcuboid2 parameters:
draftcuboid2_base_length = 26 *scaling
draftcuboid2_base_width = 21 *scaling
draftcuboid2_height = 8 *scaling
draftcuboid2_angle = 45
draftcuboid2_cylinder_radius = 1.75 *scaling
draftcuboid2_cylinder_height = 1

#draftcuboid3 parameters:
draftcuboid3_base_length = 26 *scaling
draftcuboid3_base_width = 21 *scaling
draftcuboid3_height = 8 *scaling
draftcuboid3_angle = 45
draftcuboid3_hex_radius = 2.5 *scaling
draftcuboid3_hex_height = 1 *scaling

#hexadecaprism1 parameters
hexadecaprism1_radius = 7.5 *scaling
hexadecaprism1_height = 12 

#hexadecaprism2 parameters
hexadecaprism2_radius = 7.5 *scaling
hexadecaprism2_height = 12 *scaling
hexadecaprism2_angle = 10

#hexagon1 parameters
hexagon1_base_radius = 9.31 *scaling
hexagon1_height = 8 *scaling
hexagon1_angle = 25

#hexagon2 parameters
hexagon2_base_radius = 9.31 *scaling
hexagon2_height = 8 *scaling
hexagon2_angle = 25
hexagon2_cylinder_radius = 2.5 *scaling
hexagon2_cylinder_height = 1 *scaling

#icositetragon1 parameters:
icositetragon1_base_radius = 7.5 *scaling
icositetragon1_height = 12

#icositetragon2 parameters:
icositetragon2_base_radius = 7.5 *scaling
icositetragon2_height = 12 *scaling
icositetragon2_angle = 10

#octohexapentaprism1 parameters:
octohexapentaprism1_oct_radius = 16.24 *scaling
octohexapentaprism1_oct_height = 8
octohexapentaprism1_hex_radius = 10 *scaling
octohexapentaprism1_hex_height = 6
octohexapentaprism1_pent_radius = 6.18 *scaling
octohexapentaprism1_pent_height = 5

#octohexapentaprism2 parameters:
octohexapentaprism2_oct_radius = 16.24 *scaling
octohexapentaprism2_oct_height = 8 *scaling
octohexapentaprism2_hex_radius = 10 *scaling
octohexapentaprism2_hex_height = 6 *scaling
octohexapentaprism2_pent_radius = 6.18 *scaling
octohexapentaprism2_pent_height = 5 *scaling
octohexapentaprism2_angle = 25 

#octaprism1 parameters:
octaprism1_radius = 8 *scaling
octaprism1_height = 6

#octaprism2 parameters:
octaprism2_radius = 8 *scaling
octaprism2_height = 6 *scaling
octaprism2_angle = 10

#pentaprism1 parameters
pentaprism1_radius = 5.1 *scaling
pentaprism1_height = 8 

#pentaprism2 parameters
pentaprism2_radius = 5.1 *scaling
pentaprism2_height = 8 *scaling
pentaprism2_angle = 10

#pyramidrow1 parameters:
pyramidrow1_board_length = 16 *scaling
pyramidrow1_board_width = 8 *scaling
pyramidrow1_board_height = 15
pyramidrow1_pyramid_base = 8 *scaling
pyramidrow1_angle = 35

#pyramidrow2 parameters:
pyramidrow2_board_length = 16 *scaling
pyramidrow2_board_width = 16 *scaling
pyramidrow2_board_height = 15
pyramidrow2_pyramid_base = 8 *scaling
pyramidrow2_angle = 35

pyramidrow3_base_length = 16 *scaling
pyramidrow3_base_width = 8 *scaling
pyramidrow3_base_height = 1
pyramidrow3_pyramid_length = 4 * scaling
pyramidrow3_angle = 35

#pyramidrow4 parameters:
pyramidrow4_board_length = 15 *scaling
pyramidrow4_board_width = 5 * scaling
pyramidrow4_board_height = 1
pyramidrow4_pyramid_length = 5 *scaling
pyramidrow4_angle = 10

#tetrahedron1 parameters:
tetrahedron1_length = 25 *scaling
tetrahedron1_height = 7.22 *scaling
tetrahedron1_angle = 45

#parallelogram1 parameters:
parallelogram1_length = 15 *scaling
parallelogram1_height =12
parallelogram1_angle = 45