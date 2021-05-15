from orders.models import Order
from .models import Sale
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


@receiver(post_save, sender=Order)
def post_save_create_sale(sender, instance, created, *args, **kwargs):
    if created:
        Sale.objects.create(order=instance, amount=instance.total_price)
    else:

        if Sale.objects.filter(order=instance).exists():
            order_sale = Sale.objects.get(order=instance)
            order_sale.amount = instance.total_price
            order_sale.save()
        else:
            Sale.objects.create(order=instance, amount=instance.total_price)


@receiver(pre_delete, sender=Sale)
def pre_delete_change_active_order(sender, instance, *args, **kwargs):
    obj = instance.order
    object.active = False
    pass
