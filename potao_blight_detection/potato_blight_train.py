from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
# from keras.callbacks import ModelCheckpoint

classifier = Sequential()

#1st input convolution layer
classifier.add(Convolution2D(32,kernel_size=3,input_shape=(256, 256, 3),activation='relu'))
classifier.add(MaxPooling2D( pool_size=(2,2)) )

#2nd  convolution layer
classifier.add(Convolution2D(64,kernel_size=3,activation='relu'))
classifier.add(MaxPooling2D( pool_size=(2,2)) )

#Flatten
classifier.add( Flatten())

#Fully connected layer
classifier.add( Dense( 128 , activation = 'relu') )

# Final Layer using Softmax
classifier.add(Dense(3, activation='softmax'))

#compile
# classifier.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
from keras.optimizers import SGD
opt = SGD(lr=0.01)
classifier.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
#prepocess image as input
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
                                    rescale=1./255,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
                                                  'Potato/Train',
                                                  target_size=(256, 256),
                                                  batch_size=32,
                                                  class_mode='categorical')

test_set = test_datagen.flow_from_directory(
                                            'Potato/Test',
                                            target_size=(256, 256),
                                            batch_size=32,
                                            class_mode='categorical')

#To save the best model 
filepath="my_model.h5"
# checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
# callbacks_list = [checkpoint]

classifier.fit_generator(
        training_set,
        steps_per_epoch=900,
        epochs=25,
        validation_data=test_set,
        validation_steps=300
        # callbacks=callbacks_list
        )
