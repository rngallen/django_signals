from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.db.models.fields.related import ManyToManyField
from cars.models import Car
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Order(models.Model):
    name = models.CharField(_("order description"), max_length=50)
    cars = ManyToManyField(Car, verbose_name="cars")
    total = models.PositiveIntegerField(_("total cars"), blank=True, null=True)
    total_price = models.FloatField(_("total price"), blank=True, null=True)
    active = models.BooleanField(_("active"), default=True)

    def __str__(self):
        return self.name
