from django import forms
from .models import *


class CreateForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = '__all__'

