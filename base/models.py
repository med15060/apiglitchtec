from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from django.utils import timezone

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Apply(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=255,null=True,blank=True)
    username=models.CharField(max_length=255,null=True,blank=True)
    last_name=models.CharField(max_length=255,null=True,blank=True)
    phone=models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    rate=models.CharField(max_length=255,null=True,blank=True)
    specializes=models.CharField(max_length=255,null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    conuntry=models.CharField(max_length=255,null=True,blank=True)
    state=models.CharField(max_length=255,null=True,blank=True)
    zip=models.CharField(max_length=255,null=True,blank=True)
    introduction=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg',null=True,blank=True)
    CATEGORY =(
    ('verified', 'verified'),
    ('Pending','Pending'),
    ('Declined','Declined')
    )
    account_status = models.CharField(max_length=200, null=True,choices=CATEGORY)

    def __str__(self):
        return self.user.username

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created')

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()





class Messageinfo(models.Model):
    name=models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=200, null=True)
    mess=models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.name



class Quizz(models.Model):
    name= models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=200, null=True,blank=True)
    #CATEGORY =(
    #('Red', 'Red'),
    #('Green','Green'),
    #('Blue','Blue')
    #)
    color = models.CharField(max_length=200,null=True,blank=True)
    date =  models.DateField(null=True,blank=True)
    bio = models.CharField(max_length=255,null=True,blank=True)
    food = models.CharField(max_length=255,null=True,blank=True)
    filee = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.name
