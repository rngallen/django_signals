from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Sale(models.Model):
    order = models.ForeignKey(
        "orders.Order", verbose_name=_("order"), on_delete=models.PROTECT
    )
    amount = models.FloatField(_("total amount"), blank=True, null=True)

    def __str__(self):
        return f"{self.order}"
