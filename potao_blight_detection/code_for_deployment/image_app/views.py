from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from PIL import Image 
from random import randint
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
#load model


def predict(image_path):
    #load model
    classifier = load_model('my_model.h5')
    from keras.optimizers import SGD
    opt = SGD(lr=0.01)
    classifier.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    img = image.load_img(image_path.lstrip('/'), target_size=(256, 256))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    flatten_images = np.vstack([x])
    classes = classifier.predict_classes(flatten_images)
    return 'blight' if classes == [0] else 'Healthy'
    
# Create your views here.

def image_view(request): 
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('images') 
    else: 
        form = ImageForm() 
    return render(request, 'image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 


def display_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        list_images = list(InpImage.objects.all())  
        last_image = list_images[-1]
        prediction = predict(last_image.Main_Img.url)

        return render(request, 'display_images.html', {'last_image' : last_image,'prediction':prediction}) 