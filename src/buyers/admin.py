from django.contrib import admin
from .models import Buyer
# Register your models here.


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user', 'from_signal')
