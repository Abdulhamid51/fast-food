from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Foods)
admin.site.register(OrderFood)
admin.site.register(PlaceOrder)
admin.site.register(Chefs)