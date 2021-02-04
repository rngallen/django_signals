from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyer


@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, *args, **kwargs):
    if created:
        Buyer.objects.create(user=instance)
