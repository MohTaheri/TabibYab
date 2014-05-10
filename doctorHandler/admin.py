__author__ = 'arash'


from django.contrib.gis import admin
from models import *

admin.site.register(Clinic, admin.GeoModelAdmin)
