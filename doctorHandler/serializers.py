#encoding:UTF-8
__author__ = 'arash'

from django.forms import widgets
from rest_framework import serializers
from models import *

class ClinicListSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(source='get_avg_rating', read_only=True)
    class Meta:
        model = Clinic
        write_only_fields = ('appointmentOnly','description', 'websiteAddress',)
class ClinicDetailSerializer(serializers.ModelSerializer):
    rating = serializers.DecimalField(source='get_avg_rating', read_only=True)
    waiting_time = serializers.DecimalField(source='get_avg_waiting_time', read_only=True)
    queue_time = serializers.DecimalField(source='get_avg_queuing_time', read_only=True)

    class Meta:
        model = Clinic

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment