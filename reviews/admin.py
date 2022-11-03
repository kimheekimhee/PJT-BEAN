from django.contrib import admin
from .models import Reviews, HotPlace, Location, ImageLocation, ImageHotPlace, ImageReviews
# Register your models here.


admin.site.register(Reviews)
admin.site.register(HotPlace)
admin.site.register(Location)
admin.site.register(ImageReviews)
admin.site.register(ImageHotPlace)
admin.site.register(ImageLocation)