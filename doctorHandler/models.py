#encoding:UTF-8
from django.contrib.gis.db import models

# Create your models here.


class Bussiness(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'نام')
    coordinates = models.PointField(verbose_name=u'مختصات جغرافیایی')
    objects = models.GeoManager()


class Clinic(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'نام')
    coordinates = models.PointField(verbose_name=u'مختصات جغرافیایی')
    type = models.CharField(verbose_name=u'نوع', choices=[(u'بیمارستان',u'بیمارستان'),(u'مطب',u'مطب'),(u'کلینیک',u'کلینیک')],max_length=32,null=True)
    appointmentOnly = models.CharField(verbose_name=u'نیاز به وقت قبلی', choices=[(u'بلی',u'بلی'),(u'خیر',u'خیر')],max_length=16, null=True)
    # profileImage = models.ImageField(verbose_name=u'عکس پروفایل')
    objects = models.GeoManager()

class Comment(models.Model):
    clinic = models.ForeignKey(Clinic)
    name = models.CharField(max_length=200, verbose_name=u'نام')
    comment = models.CharField(max_length=200, verbose_name=u'نظر')
    object = models.GeoManager()