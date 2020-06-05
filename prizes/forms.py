from django import forms
from . import models

class CreatePrize(forms.ModelForm):
    class Meta:
        model = models.Prize
        fields = '__all__'
