__author__ = 'arash'


from django.contrib.gis import admin
from models import *

admin.site.register(Bussiness, admin.GeoModelAdmin)
admin.site.register(Clinic, admin.GeoModelAdmin)