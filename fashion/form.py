from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Image , Review ,Profile
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_photo' , 'image_name' ,'description')

class ProfileForm(forms.ModelForm):
    class Meta:
          model = Profile
          fields = ('user' ,'profile_photo' ,'bio')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body' ,'post' ,'name')
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('username' , 'first_name' ,'last_name', 'email' )   