#encoding:UTF-8
from django.contrib.gis.db import models
import os
from uuid import uuid4
# Create your models here.
from django.db.models.aggregates import Avg


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


class Clinic(models.Model):
    name = models.CharField(max_length=200,verbose_name=u'نام')
    coordinates = models.PointField(verbose_name=u'مختصات جغرافیایی')
    type = models.CharField(verbose_name=u'نوع', max_length=32,null=True)
    speciality_level = models.CharField(verbose_name=u'درجه تخصص', max_length=32, null=True)
    speciality = models.CharField(verbose_name=u'تخصص', max_length=32, null=True)
    appointmentOnly = models.CharField(verbose_name=u'نیاز به وقت قبلی', max_length=16, null=True)
    websiteAddress = models.CharField(max_length=200,verbose_name=u'آدرس وب سایت', null=True)
    address = models.CharField(max_length=200,verbose_name=u'آدرس', null=True)
    description = models.CharField(max_length=200,verbose_name=u'توضیحات', null=True)
    profileImage = models.ImageField(verbose_name=u'عکس پروفایل',upload_to=path_and_rename('media/profilePics'), null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1,verbose_name=u'امتیاز',default=0)
    comment_num = models.IntegerField(verbose_name='تعداد نظر‌ها',default=0)
    objects = models.GeoManager()

    # def get_avg_rating(self):
     #    average = Comment.objects.all().filter(clinic = self.id).aggregate(avg=Avg('rating'))
	# if average['avg'] != None :
	#         return average['avg']
	# else :
	# 	return 0

    def get_avg_waiting_time(self):
        average = Comment.objects.all().filter(clinic = self.id).aggregate(avg=Avg('waiting_time'))
        return average['avg']
		
		
    def get_avg_queuing_time(self):
        average = Comment.objects.all().filter(clinic = self.id).aggregate(avg=Avg('queue_time'))
        return average['avg']
    	
    def get_avg_visiting_fee(self):
        average = Comment.objects.all().filter(clinic = self.id).aggregate(avg=Avg('price'))
        return average['avg']


class Comment(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='comments')
    name = models.CharField(max_length=200, verbose_name=u'نام', null=True)
    comment = models.CharField(max_length=200, verbose_name=u'نظر')
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True,verbose_name=u'امتیاز')
    date = models.DateTimeField(auto_now=True, verbose_name=u'تاریخ و زمان')
    staff_attitude_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True,verbose_name=u'امتیاز رفتار کارکنان')
    doctor_attitude_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True,verbose_name=u'امتیاز رفتار دکتر')
    treatment_result_rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True,verbose_name=u'رضایت از نتیجه درمان')
    price = models.DecimalField(max_digits=9, decimal_places=1, blank=True, null=True,verbose_name=u'هزینه ویزیت')
    waiting_time = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,verbose_name=u'زمان انتظار در مطب')
    queue_time = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,verbose_name=u'زمان انتظار برای وقت دادن')
    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        if self.pk is None :
            super(Comment, self).save(*args, **kwargs)
            oldSum = self.clinic.rating * self.clinic.comment_num
            self.clinic.comment_num += 1
            newSum = oldSum + self.rating
            self.clinic.rating = newSum / self.clinic.comment_num
            self.clinic.save()
        else :
            oldComment = Comment.objects.get(pk=self.pk)
            dt = self.rating - oldComment.rating
            oldSum = self.clinic.rating * self.clinic.comment_num
            newSum = oldSum + dt
            self.clinic.rating = newSum / self.clinic.comment_num
            self.clinic.save()
            super(Comment, self).save(*args, **kwargs)

    def delete(self, using=None):
        oldSum = self.clinic.rating * self.clinic.comment_num
        self.clinic.comment_num -= 1
        newSum = oldSum - self.rating
        self.clinic.rating = newSum / self.clinic.comment_num
        self.clinic.save()
        super(Comment, self).delete()


class PhoneNumber(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='phone_numbers')
    title = models.CharField(max_length=200, verbose_name=u'عنوان')
    tel = models.CharField(max_length=200, verbose_name=u'شماره تلفن')

class OperatingHours(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='operating_hours')
    fromTime = models.TimeField(verbose_name=u'از زمان')
    toTime = models.TimeField(verbose_name=u'تا زمان')

class Picture(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='pictures')
    title = models.CharField(max_length=200, verbose_name=u'عنوان')
    pic = models.ImageField(verbose_name=u'عکس پروفایل',upload_to=path_and_rename('media/pics'))


class Insurance(models.Model):
    clinic = models.ForeignKey(Clinic, related_name='insurances')
    title = models.CharField(max_length=200, verbose_name=u'عنوان')
