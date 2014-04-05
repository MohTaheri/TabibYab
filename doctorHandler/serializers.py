#encoding:UTF-8
__author__ = 'arash'

from django.forms import widgets
from rest_framework import serializers
from models import *

class ClinicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
class ClinicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment