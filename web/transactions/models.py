from django.db import models
from django.contrib.postgres.fields import ArrayField
from search.customModels import IntegerRangeField
from jsonfield import JSONField


class Schedule(models.Model):
    pageId = models.CharField(max_length=400, null=True)
    date = models.DateTimeField(auto_now=True)
    sessions = ArrayField(models.CharField(max_length=50), null=True)
    def __str__(self):
        return self.id

class MerchantEndpointLink(models.Model):
    merchant = models.CharField(max_length=400, primary_key = True)
    endPoints = ArrayField(models.CharField(max_length=50), null=True)

class SessionEndpoint(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    spots = models.IntegerField(default=-1)
    datetime = models.DateTimeField(auto_now=False,null=True)
    pageId = models.CharField(max_length=400, null=True)
    def __str__(self):
        return self.id

class Session(models.Model):
    id = models.CharField(max_length=400, primary_key=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    users = JSONField()
    pub = models.CharField(max_length=1024,default='')
    priv= models.CharField(max_length=1024,default='')

    def __str__(self):
        return self.id
