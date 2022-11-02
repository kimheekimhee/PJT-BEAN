from django import forms
from django import forms
from .models import Reviews, HotPlace, Location

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'grade', ]

class HotPlaceForm(forms.ModelForm):
    class Meta:
        model = HotPlace
        fields = ['hotplace', 'addr', 'theme', 'country', 'content', 'x', 'y' ]
