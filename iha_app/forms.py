from django import forms
from .models import IHA, Kiralama

class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = '__all__'

class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = '__all__'
