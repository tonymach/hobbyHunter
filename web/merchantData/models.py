from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

class MerchantData(models.Model):
    id = models.ManyToOneRel(User, primary_key=True)
    trial = models.BooleanField(default=True)
    isActive = models.BooleanField(default=False)
    SessionCount = models.IntegerField(default=0)
    UserSessionCount = models.IntegerField(default=0)
    PaymentToken = models.CharField(max_length=800)
