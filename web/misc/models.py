from django.db import models

class tryMe(models.Model):
    thing = models.CharField(max_length=300)
