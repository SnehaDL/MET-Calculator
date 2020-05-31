from django import forms
from .models import bmrtable,mettable

class BMRForm(forms.ModelForm):
    class Meta :
        model  = bmrtable
        fields = ('age','weight',
                'height','gender')

class METForm(forms.ModelForm):
    class Meta :
        model  = mettable
        fields = ('activity','level',
                'hours','minutes')
