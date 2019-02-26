from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField
from search.customModels import IntegerRangeField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Page(models.Model):

    pageId = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=100)
    stars = models.IntegerField(null=True)
    createdOn = models.DateField(auto_now=True)
    description = models.CharField(max_length=2000,null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    averageCost = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    country = models.CharField(max_length=2)
    mainImage = models.FileField(upload_to = 'merchant/main/', default = 'no-img.jpg',null=True)
    mainImage_thumbnail = ImageSpecField(source='mainImage',
                                      processors=[ResizeToFill(125, 125)],
                                      format='JPEG',
                                      options={'quality': 60})

    secondaryImage = models.FileField(upload_to = 'merchant/secondary/', default = 'no-img.jpg',null=True)
    ThirdImage = models.FileField(upload_to = 'merchant/third/', default = 'no-img.jpg',null=True)
    merchant = models.CharField(max_length=200, null=True)

    # reviews = models.ManyToManyField(Review)
    def __str__(self):
        return self.pageId

class Search(models.Model):
    keywords = ArrayField(models.CharField(max_length=200), blank=True)
    models.ManyToManyField(Page)
    def __str__(self):
        return self.id

class Keyword(models.Model):
    keyword = models.CharField(max_length=200, primary_key=True)
    pages = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    def __str__(self):
        return self.keyword


class Index(models.Model):
    search = models.CharField(max_length=650, primary_key=True)
    endPoints = ArrayField(models.CharField(max_length=200),blank=True)
    def __str__(self):
        return self.search

class merchantPages(models.Model):
    merchant = models.CharField(max_length=200, primary_key=True)
    endPoints = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    def __str__(self):
        return self.merchant
