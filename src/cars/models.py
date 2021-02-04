from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

# Create your models here.


class Car(models.Model):
    name = models.CharField(_("name"), max_length=50)
    price = models.FloatField(_("price"))
    buyer = models.ForeignKey("buyers.Buyer", verbose_name=_(
        "buyer"), on_delete=models.CASCADE, related_name='car_buyer')
    code = models.CharField(_("code"), max_length=10, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.buyer}"

    # def save(self, *args, **kwargs):
    #     if not self.code:
    #         self.code = str(uuid.uuid4()).replace("-","").upper()[:10]
    #         return super().save(*args, **kwargs)
