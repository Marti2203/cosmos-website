from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_nr = models.CharField(max_length=15)
    tue_id = models.CharField(max_length=25)
    card_number = models.CharField(max_length=25)
    key_access = models.CharField(max_length=3)
    member_type = models.CharField(max_length=50)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except:
        Profile.objects.create(user=instance)
