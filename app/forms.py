from django import forms
from .models import *

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']