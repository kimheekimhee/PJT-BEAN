from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Location(models.Model):
    location = models.CharField(max_length=80)
    country = models.BooleanField(default=True)

class ImageLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='image')
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 80})
    
    
class HotPlace(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hotplace')
    hotplace = models.CharField(max_length=100)
    addr = models.CharField(max_length=80)
    x = models.CharField(max_length=80, blank=True, null=True)
    y = models.CharField(max_length=80, blank=True, null=True)
    theme = models.CharField(max_length=80)
    country = models.CharField(max_length=50)
    content = models.TextField()

class ImageHotPlace(models.Model):
    hotplace = models.ForeignKey(HotPlace, on_delete=models.CASCADE, related_name='image')
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 80})

class Reviews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotplace = models.ForeignKey(HotPlace, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    grade = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ImageReviews(models.Model):
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='image')
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(1200, 960)],
                                format='JPEG',
                                options={'quality': 80})
    image_thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(200, 200)],
                                format='JPEG',
                                options={'quality': 60})