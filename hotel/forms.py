from django import forms
from django.db.models import fields
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name', 'price', 'city', 'rating',)

class HotelFormNew(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    price = forms.IntegerField(min_value=1, max_value=999999, required=False)
    city = forms.CharField(max_length=30, required=False)
    rating = forms.IntegerField(min_value=1, max_value=10, required=False)

