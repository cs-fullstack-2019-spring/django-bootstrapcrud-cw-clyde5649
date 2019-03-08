from django import forms
from .models import GarageSellmodel


class GarageSellform(forms.ModelForm):
    class Meta:
        model = GarageSellmodel
        fields = '__all__'
