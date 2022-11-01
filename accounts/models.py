from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
    image = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[Thumbnail(60, 60)],
                                format='JPEG',
                                options={'quality':90})

    @property
    def full_name(self):
        return f"{self.last_name}{self.first_name}"
