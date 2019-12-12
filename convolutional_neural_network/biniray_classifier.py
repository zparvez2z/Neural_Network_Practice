from keras.model import Sequential
from keras.model import Convolution2D
from keras.model import MaxPooling2D
from keras.model import Flatten
from keras.model import Dense

classifier = Sequential()

classifier.add( Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu') )

classifier.add(MaxPoiling2D( pool_size=(2,2)) )

classifier.add( Flatten())

classifier.add( Dense( output_dim=128 , activation = 'relu') )
classifier.add( Dense( output_dim=1 , activation = 'sigmoid') )

classifier.compile( optimizer='adam' , loss='binary_crossentropy', metrics=['accuracy'])


keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
                                                  'data/train',
                                                  target_size=(64,64),
                                                  batch_size=32,
                                                  class_mode='binary')

test_set = test_datagen.flow_from_directory(
                                            'data/test',
                                            target_size=(64, 54),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=25,
        validation_data=test_set,
        validation_steps=2000)
