from django import forms
from medilabapp.models import Registration, ImageModel


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']
