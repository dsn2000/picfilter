from django import forms
from models import *

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()

class PicForm(forms.ModelForm):
    class Meta:
        model = Pic
        
class FiltForm(forms.ModelForm):
    class Meta:
        model = Filt