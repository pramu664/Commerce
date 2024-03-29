from django.db import models
from django import forms
from django.forms import fields, ModelForm, HiddenInput
from django.utils import timezone

from .models import Listing, User, Profile

class ListingForm(ModelForm):

    date = forms.DateTimeField(initial=timezone.now(), widget=forms.HiddenInput)
    author = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Listing
        fields = ["title", "content", "date", "author", "image", "price", "listing_categories" ]
    

class BiddingForm(forms.Form):
    bid = forms.IntegerField()

class CommentForm(forms.Form):
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))

# -> Updating the Profile forms

# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["image"]

