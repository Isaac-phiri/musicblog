from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Song
class UploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('title','artist', 'image', 'file')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

