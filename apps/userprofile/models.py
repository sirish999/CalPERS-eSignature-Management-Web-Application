from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name='custom_user_profile', on_delete=models.CASCADE)
    pref_name = models.CharField(
        max_length=30, null=True, blank=True)
    bio = models.TextField(
        max_length=500,  blank=True)
    phone_number = models.CharField(
        max_length=12, blank=True)
    birth_date = models.DateField(
        null=True, blank=True)
    profile_image = models.ImageField(
        default='default-avatar.png', upload_to='users/', null=True, blank=True)
    signature_store = models.TextField(
        max_length=650000,  blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
