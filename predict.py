import matplotlib.pyplot as plt
import numpy as np
from variables import scaling, px, centre, X_mm, Y_mm
from tensorflow.keras.models import load_model
from plot import plot_surface
from preprocess import preprocess, load_experimental_data


name = "octohexaprism"
number = 2

rev = 207

unseen_path = "C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/2510_trial/octohexaprism2_2510"
unseen_path = "C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/1911_trial/hexagon2_1911"
unseen_path = "C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/1911_trial/torus1_1911"
unseen_path = "C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/1911_trial/pyramidrow1_1911"
#unseen_path = "C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/2510_trial/octohexapentaprism1_2510"
#unseen_path = "C:/Users/dwint/OneDrive/Desktop/Fourth Year/(SEM1) Capstone Project/data/2510_trial/steppyramid1_2510"

raw_imgs, unseen_pics = preprocess(px, gallery=load_experimental_data(unseen_path))

plt.imshow(raw_imgs[7])
plt.title(f"Unseen Object {name}({number})")
plt.xlabel("X [px]")
plt.ylabel("Y [px]")
plt.show()

#Load model
diverse_model = load_model(f"combined_test_rev{rev}.keras")

#Make predictions on unseen data
predicted_output = diverse_model.predict(unseen_pics)

diverse_model.summary()

#Turn to heightmap (HxW)
predicted_heightmap = np.squeeze(predicted_output, axis=0)
predicted_heightmap = np.squeeze(predicted_heightmap, axis=-1)
print(predicted_heightmap.shape)

plot_surface(X_mm, Y_mm, predicted_heightmap, f"Rev#{rev} Prediction of {name}({number})",zlim=1)

