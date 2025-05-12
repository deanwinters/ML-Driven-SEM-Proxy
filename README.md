# Machine Learning Driven Proxy for Scanning Electron Microscopy using Multi-illumination Capture to Emulate Nano-tomography

This repo contains the source code for my capstone project based on an optical proxy of SEM. This is by multi-illumination using an Arduino and custom-built apparatus with 20 LEDs captures the shadows cast by sample objects due to its surface profile. This data then trains a deep learning model for prediction on unseen object or surface profiles.

Google Drive of other relevant items: [https://drive.google.com/drive/folders/1yPZz08AGPmr1m3wZQ8gY_qqawLh73cRo?usp=sharing].

Contact: deanpwinters@gmail.com ; dwinters@tcd.ie

### Apparatus:

*arduino_sketch.ino* contains the serial communication passed to the Arduino MEGA board to control each LED. With the Arduino powered via. USB to the host PC, *capture.py* works to send these commands across using pyserial. With the microscope camera also connected via USB (or other means for opencv) then each LED is turned on, an image captured, and turned off, for each of the 20 LEDs. Currently the experimental data captured is stored locally.

### Code workflow:

The project follows supervised network training. Training labels ("ground-truth based labels", or shorthand "gtb") for each sample object are stored in ./labels/. These are the actual heightmap recreations of the sample objects, and are given to the model for validation when training. Currently there are ~35-40 of these arbitrarily created sample objects printed, but more were made and found printing difficulty; all of this was done in Solidworks and variation of surface profiles was the only consideration with these. The part files can be found in the Drive.

The experimental data using the printed sample objects can be found in the Drive (~14GB). *train_setup.py* pulls the data locally and considers each of the 20 image bundles, and performs augmentation to create more virtual datasets to diversify training and familiarise the neural network with orientation (see: *preprocess.py*). This experimental data is then bundled together into one dataset, and similarly the gtb data. Five experimental sets, *steppyramid1, torus1, random1, pyramidrow1, hexagon2* are currently withheld as the unseen objects for report results.

These sets are passed to *train.py* to train the *cnn.py* model, a U-Net architecture CNN, on the experimental and gtb data. The different training parameters are worth tweaking more; I find that given the relatively small training dataset available it becomes very easy for the model to overfit information as opposed to real predictive behaviour. Also given the augmentation it becomes quite hard to train over many epochs, but this may not be as big an issue with backpropagation. Some results with different parameters are shown in the Drive.

### Going forward:

Larger training data is desireable. Obviously one way is to continue further with more object design and printing, and heightmap creations. A key issue with this is that it's a cumbersome process that will not yield a great deal of data; one alternative not sought after was doing this process in conjunction with virtual training using rendering software. For example, Blender would allow for a replica of the apparatus with LEDs and a camera without the need for printing each design. If more sample objects could be designed in Blender, and heightmap renders exported to Python for training, this would streamline the process and negate the need to manually build each heightmap (unless there exists a workaround using a Solidworks-Python mesh export).

Something else of note was a similar approach by training on procedurally-generated object meshes, starting with primitive shapes like cubes, then evolving to a cube with a sphere attached, etc. This would allow for far greater sample shape diversity, and quantity. Seen in: [https://ieeexplore.ieee.org/document/8578496] (D. Yang and J. Deng, "Shape from Shading Through Shape Evolution," 2018).








