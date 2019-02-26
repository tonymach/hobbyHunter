from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Choice(models.Model):
    skill = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    mainImage = models.FileField(upload_to = 'choice/main/', default = 'no-img.jpg',null=True)
    mainImage_thumbnail = ImageSpecField(source='mainImage',
                                      processors=[ResizeToFill(250, 155)],
                                      format='JPEG',
                                      options={'quality': 40})
