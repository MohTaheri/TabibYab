#encoding:UTF-8
__author__ = 'arash'

from django.forms import widgets
from rest_framework import serializers
from models import *

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        write_only_fields = ('date','staff_attitude_rating','doctor_attitude_rating','treatment_result_rating','price','waiting_time','queue_time')

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber

class OperatingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingHours

class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture

class InsurancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance


class ClinicListSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(source='get_avg_rating', read_only=True)
    class Meta:
        model = Clinic
        write_only_fields = ('appointmentOnly','description', 'websiteAddress',)
class ClinicDetailSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(source='get_avg_rating', read_only=True)
    waiting_time = serializers.DecimalField(source='get_avg_waiting_time', read_only=True)
    queue_time = serializers.DecimalField(source='get_avg_queuing_time', read_only=True)

    phone_numbers = PhoneNumberSerializer(many=True)
    operating_hours = OperatingHoursSerializer(many=True)
    pictures = PicturesSerializer(many=True)
    insurances = InsurancesSerializer(many=True)


    class Meta:
        model = Clinic




