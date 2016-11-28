from django.contrib import admin

from .models import Order, Project, TradeType
# Register your models here.

admin.site.register(Order)
admin.site.register(Project)
admin.site.register(TradeType)

