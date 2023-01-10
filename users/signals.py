from django.db.models.signals import (m2m_changed, pre_save, post_save, post_delete, pre_delete )
from django.contrib.auth.models import User, Group
from django.dispatch import receiver

from .models import Profile

# create user profile whenever user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance,  created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# on profile delete modify profile job count
@receiver(post_delete, sender=Profile)
def delete_task(sender,instance,*args,**kwargs):
    print('hi')

# create location for user profile
@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance,  created, *args, **kwargs):
    if created:
        profile_location = Location.objects.create()
        instance.location=profile_location
        instance.save()