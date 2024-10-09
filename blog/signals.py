from django.db.models.signals import post_save
from django.contrib.auth import get_user_model, user_logged_in
from django.dispatch import receiver
from .models import Profile
from .views import info_message

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def user_logged_in(sender, request, user, **kwargs):
    info_message(request, f"Welcome back, {user.username}!")