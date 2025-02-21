from django import forms
from .models import Card

class CardForm(forms.Form):
    num = forms.IntegerField(required=True)
    cvv = forms.CharField(max_length=4, required=True)