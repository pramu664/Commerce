from django.db import models
from django import forms
from django.forms import fields, ModelForm, HiddenInput
from django.utils import timezone

from .models import Listing, User

class ListingForm(ModelForm):

    date = forms.DateTimeField(initial=timezone.now(), widget=forms.HiddenInput)
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Listing
        fields = ["title", "content", "date", "author", "image" ]

