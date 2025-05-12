from imports import *
from variables import scaling, px, centre
from cnn import CNN
from train_setup import combined_data, combined_gtb

#Call model
dims = (px,px, 20) #size of images it expects to take
model = CNN(dims)
model.compile(optimizer=Adam(learning_rate=1e-4), loss="mse")
model.summary()

#Train model on the combined dataset
training = model.fit(combined_data, combined_gtb,
                    validation_split=0.2,
                    epochs=6,
                    batch_size=10
                   )

#Save trained model
model.save("combined_test_rev208.keras")

#Plot training loss
#This training/validation metric based on the evaluation function of the CNN 
#and compiler respectively doesn't seem to offer much of substance,
#you could predict a great shape recovery yet a lot of noise and it may be technically less valid
#than a completely blank prediction
plt.title("Training Loss")
plt.xlabel("No of Epochs")
plt.ylabel("Loss%")
plt.plot(training.history["loss"], label="Training Loss")
plt.plot(training.history["val_loss"], label="Validation Loss")
plt.show()
