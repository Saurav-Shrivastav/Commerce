from django import forms

from .models import *


class CreateListingForm(forms.ModelForm):
    '''A form to create listings'''
    class Meta:
        model = Listing
        exclude = ("created_by", )