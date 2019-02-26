from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
# from .managers import UserManager

from django.contrib.postgres.fields import ArrayField
from search.customModels import IntegerRangeField
from jsonfield import JSONField



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # If type is U - User, type M - merchant, type X - NeoManiac{Me}
    accType = models.CharField(max_length=1,default='U')
    # Link to the profile picture
    img_avatar = models.CharField(max_length=128, null=True)

    phone_number = models.IntegerField(null=True)

    # LOCATION
    # Signup location
    location = models.CharField(max_length=80, blank=True, null=True)
    location_active = models.CharField(max_length=80, blank=True, null=True)
    location_active_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    location_active_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    # User only

    user_firstname = models.CharField(max_length=50, default='')
    user_lastname = models.CharField(max_length=50, default='')
    # Class ids previously taken
    user_previouslyTaken = ArrayField(models.CharField(max_length=200, default=''), blank=True, null=True)
    # Either generated or pulled from taken, will take care of in the future

    user_classKeys =  JSONField(default='')

    # Merchant Biography
    merchant_description = models.TextField(max_length=50000, blank=True)

    #Transactional things will be held seperately
    payment_id = models.CharField(max_length=128, default='')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def accountType(self):
        return self.accType

    def is_merchant(self):
        if self.accType == 'M':
            return True
        else:
            return False

    def is_user(self):
        if self.accType == 'U':
            return True
        else:
            return False

    def GetclassKeys(self):
        return self.user_classKeys
