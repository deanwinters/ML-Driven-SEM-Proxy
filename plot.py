# Plotting function used to visually validate each heightmap label, and visually show the neural net predictions

import matplotlib.pyplot as plt

def plot_surface(X_mm, Y_mm, heightmap, name,zlim):
    #plt.figure(figsize=(12,8))
    plt.imshow(heightmap)
    plt.colorbar(label="Normalised Height")
    plt.title(f"Recovered 2D Heightmap of {name}")
    plt.xlabel("X [px]")
    plt.ylabel("Y [px]")
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    ax.plot_surface(X_mm, Y_mm, heightmap, cmap="viridis", edgecolor="none")
    ax.set_title(f"Recovered 3D Surface of {name}")
    ax.set_xlabel("X [mm]")
    ax.set_ylabel("Y [mm]")
    ax.set_zlabel("Normalised Height")
    # ax.set_xlim(0,30)
    # ax.set_ylim(0,30)
    ax.set_zlim(0,zlim)
    plt.show()
