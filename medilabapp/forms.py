from django import forms
from medilabapp.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']
