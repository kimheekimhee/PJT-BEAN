from django import forms
from django import forms
from .models import Reviews, HotPlace

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'image', 'grade', ]

class HotPlaceForm(forms.ModelForm):
    class Meta:
        model = HotPlace
        fields = ['hotplace', 'addr', 'theme', 'country', 'content', ]