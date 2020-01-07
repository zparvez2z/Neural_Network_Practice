from django import forms 
from .models import *
  
class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = InpImage 
        fields = ['name', 'Main_Img'] 