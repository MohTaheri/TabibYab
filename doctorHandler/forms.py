# -*- coding:utf-8 -*-
__author__ = 'arash'

from django.contrib.gis import forms

from models import *
class searchForm(forms.Form):
    name = forms.CharField(max_length=200, label=u'نام')
    longitude = forms.DecimalField(label='longitude')
    latitude = forms.DecimalField(label='latitude')
