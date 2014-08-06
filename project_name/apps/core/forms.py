# -*- coding: utf-8 -*-

from django import forms

from .models import ModelName

class ModelNameForm(forms.ModelForm):
    class Meta:
        model = ModelName
