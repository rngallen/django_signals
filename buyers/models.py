from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Buyer(models.Model):
    user = models.OneToOneField(User, verbose_name=_("buyer"), on_delete=models.PROTECT)
    from_signal = models.BooleanField(_("from signal"), default=False)

    def __str__(self):
        return f"{self.user}"
