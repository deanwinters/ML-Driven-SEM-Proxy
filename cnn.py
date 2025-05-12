from variables import scaling,px 
from tensorflow.keras.layers import Input, Conv2D, Conv2DTranspose, BatchNormalization, MaxPooling2D, Concatenate, Dropout
from tensorflow.keras.models import Model


#Unet3 FINAL CONCISE CODE

# (5,5) instead of (3,3) kernels were tried, but smaller kernel grid seemed to recover better features.
# Other activation funcs, e.g.:, leaky relu, might be of interest to try
# Code follows fairly standard UNet implementations seen in tutorials like pyimagesearch.com, tensorflow.org

def CNN(input_shape):
    #Model input
    x = Input(input_shape)

    #Encoder - feature extraction and dimensional reduction
    convo_1 = Conv2D(64, (3,3), activation="relu", padding="same")(x) # "same" padding may actually be the default
    convo_1 = BatchNormalization()(convo_1)
    convo_1 = Conv2D(64, (3,3), activation="relu", padding="same")(convo_1)
    pooling1 = MaxPooling2D((2,2))(convo_1)
    
    convo_2 = Conv2D(128, (3,3), activation="relu", padding="same")(pooling1)
    convo_2 = BatchNormalization()(convo_2)
    convo_2 = Conv2D(128, (3,3), activation="relu", padding="same")(convo_2)
    pooling2 = MaxPooling2D((2,2))(convo_2)
    
    convo_3 = Conv2D(256, (3,3), activation="relu", padding="same")(pooling2)
    convo_3 = BatchNormalization()(convo_3)
    convo_3 = Conv2D(256, (3,3), activation="relu", padding="same")(convo_3)
    pooling3 = MaxPooling2D((2,2))(convo_3)

    #Bottleneck with dropout
    #bottleneck = Conv2D(512, (5,5), activation="relu", padding="same")(pooling3) #5,5 for wider-scale feature retention?
    bottleneck = Conv2D(512, (3,3), activation="relu", padding="same")(pooling3)
    bottleneck = Dropout(0.7)(bottleneck) # High dropout helps to prevent overftting - problem with small dataset
    bottleneck = BatchNormalization()(bottleneck)
    
    #Decoder - dimensional upsampling, skip connections, and more feature extraction
    upsample1 = Conv2DTranspose(256, (3,3), strides=(2,2), padding="same")(bottleneck)
    upsample1 = Concatenate()([upsample1, convo_3]) # skip connection
    convo_4 = Conv2D(256, (3,3), activation="relu", padding="same")(upsample1) # Convolves to refine the features
    convo_4 = BatchNormalization()(convo_4)

    upsample2 = Conv2DTranspose(128, (3,3), strides=(2,2), padding="same")(convo_4)
    upsample2 = Concatenate()([upsample2, convo_2])
    convo_5 = Conv2D(128, (3,3), activation="relu", padding="same")(upsample2)
    convo_5 = BatchNormalization()(convo_5)

    upsample3 = Conv2DTranspose(64, (3,3), strides=(2,2), padding="same")(convo_5)
    upsample3 = Concatenate()([upsample3, convo_1])
    convo_6 = Conv2D(64, (3,3), activation="relu", padding="same")(upsample3)
    convo_6 = BatchNormalization()(convo_6)
    
    #Output layer - single channel and sigmoid activation func.
    y = Conv2D(1, (1,1), activation="sigmoid")(convo_6) # could use softmax
    
    model = Model(x, y)
    return model

