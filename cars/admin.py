from django.contrib import admin

from cars.models import Car
from .models import Car

# Register your models here.

admin.site.register(Car)