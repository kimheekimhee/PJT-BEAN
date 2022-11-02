from django import forms
from django import forms
from .models import Reviews, HotPlace, Location, ImageHotPlace, ImageReviews
from django.forms import ClearableFileInput

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'grade', ]

class HotPlaceForm(forms.ModelForm):
    class Meta:
        model = HotPlace
        fields = ['hotplace', 'addr', 'theme', 'country', 'content', 'x', 'y', ]

class HotPlaceImageForm(forms.ModelForm):
    class Meta:
        model = ImageHotPlace
        fields = ['image', ]
        widgets = {
            "image": ClearableFileInput(attrs={"multiple": True}),
        }

class ReivewImageForm(forms.ModelForm):
    class Meta:
        model = ImageReviews
        fields = ['reviews', 'image', ]