from typing import ClassVar
from django.db import models
# To create a Custom User Model and Admin Panel 
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy
# To automatically create one to one object 
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.utils.translation import gettext_lazy as _
# Create your models here.

class MyUserManager(BaseUserManager):
    # A custom Manager to deal with emails unique identifer 
    def _create_user(self,email,password,**extra_fields):
        # Creates and saves a user with a given email and password 
        if not email:
            raise ValueError('The email must be set!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email , password, **extra_fields):
        extra_fields .setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser= True')
        return self._create_user(email,password,**extra_fields)

class User (AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True,null=False)
    is_staff = models.BooleanField(
        ugettext_lazy('staff status'),
        default=False,
        help_text=ugettext_lazy('Designates whether the user can log in this site')
    )
    is_active = models.BooleanField(
        ugettext_lazy('active'),
        default=True,
        help_text=ugettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts')
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE , related_name='profile')
    username = models.CharField(max_length=264, blank=True, null=True)
    full_name = models.CharField(max_length=264, blank=True, null=True)
    address_1 = models.TextField(max_length=300,blank=True, null=True)
    class cityname(models.TextChoices):
        DHAKA = 'DHAKA', _('DHAKA')
        RANGPUR = 'RANGPUR', _('RANGPUR')
        RAJSHIE = 'RAJSHIE', _('RAJSHIE')
        KULNA = 'KULNA', _('KULNA')
        BORISAL = 'BORISAL', _('BORISAL')
    city = models.CharField(
        max_length=60,
        choices=cityname.choices,
        default=cityname.DHAKA,
        blank=True, null=True
    )

    zipcode = models.CharField(max_length=8,blank=True, null=True)

    COUNTRY_NAME = (
        ('BSANGLADESH','BSANGLADESH'),
        ('INDA','INDA'),
    )
    country = models.CharField(max_length=60, choices=COUNTRY_NAME, blank=True, null=True)
    phone = models.CharField(max_length=12,blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]

        for fields_name in fields_names:
            value = getattr(self, fields_name)
            if value is None or value=='':
                return False
        return True
  


@receiver(post_save,sender=User)
def create_profile( sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
