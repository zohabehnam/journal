from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import News


class Category(ModelForm):
    class Meta:

        model = News
        fields = ['catname']

    category = forms.ModelMultipleChoiceField

