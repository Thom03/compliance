from django.contrib import admin
from django.contrib.gis import gdal
from django.contrib.gis import admin

# Register your models here.

from .models import  *

admin.site.register(Viwandani, admin.OSMGeoAdmin)