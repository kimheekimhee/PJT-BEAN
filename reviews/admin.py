from django.contrib import admin
from .models import Reviews, HotPlace, Location, ImageLocation, ImageHotPlace, ImageReviews
# Register your models here.

class Reviewsadmin(admin.ModelAdmin):
    list_display = ['hotplace', 'title', 'created_at' ]

class Hotplaceadmin(admin.ModelAdmin):
    list_display =  ['location', 'hotplace', 'theme' ]

class Locationadmin(admin.ModelAdmin):
    list_display = ['location']

class ImageReviewsadmin(admin.ModelAdmin):
    list_display = ['reviews']

class ImageHotPlaceadmin(admin.ModelAdmin):
    list_display = ['hotplace']

class ImageLocationadmin(admin.ModelAdmin):
    list_display = ['location']



admin.site.register(Reviews, Reviewsadmin)
admin.site.register(HotPlace, Hotplaceadmin)
admin.site.register(Location, Locationadmin)
admin.site.register(ImageReviews, ImageReviewsadmin)
admin.site.register(ImageHotPlace, ImageHotPlaceadmin)
admin.site.register(ImageLocation, ImageLocationadmin)