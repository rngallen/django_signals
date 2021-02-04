from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import Car
from buyers.models import Buyer
import uuid


@receiver(pre_save, sender=Car)
def pre_save_create_code(sender, instance, *args, **kwargs):
    if not instance.code:
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
    obj = Buyer.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()
