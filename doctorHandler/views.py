# Create your views here.
import django_filters
from forms import *
from django.contrib.gis.measure import D
from models import *
from rest_framework import generics
from rest_framework import filters
from serializers import *
from decimal import *
from django.contrib.gis.geos import *
from django.db.models import Q
from django import db
import operator


class doctorsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='contains')
    class Meta:
        model = Clinic
        fields = ['name','speciality_level','speciality','type',]


class doctorsListView(generics.ListCreateAPIView):
    model = Clinic
    serializer_class = ClinicListSerializer
    filter_class = doctorsFilter
    ordering_fields = '__all__'

    def get_queryset(self):

        query_set = Clinic.objects.all()
        if self.request.GET.__contains__('lat') and self.request.GET.__contains__('lng') and self.request.GET.__contains__('dist'):
            lat = self.request.GET['lat']
            long = self.request.GET['lng']
            dist = self.request.GET['dist']
            pnt = fromstr('POINT('+lat+' ' +long+')', srid=4326)
            if self.request.GET.__contains__('orderby'):
                orderBy = self.request.GET['orderby']
                if orderBy == 'd':
                    query_set = query_set.filter(coordinates__distance_lte=(pnt, D(km=dist))).distance(pnt).order_by('distance')
                else:
                    query_set = query_set.filter(coordinates__distance_lte=(pnt, D(km=dist))).order_by('rating')
                    # query_set = query_set.reverse()
            else:
                query_set = query_set.filter(coordinates__distance_lte=(pnt, D(km=dist)))

        if self.request.GET.__contains__('orderby'):
            orderBy = self.request.GET['orderby']
            if orderBy == 'r':
                query_set = query_set.order_by('rating')
                query_set = query_set.reverse()


        return query_set


class doctorDetailView(generics.RetrieveUpdateDestroyAPIView) :
    model = Clinic
    serializer_class = ClinicDetailSerializer





class commentsFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['clinic']


class commentListView(generics.ListCreateAPIView):
    model = Comment
    serializer_class = CommentListSerializer
    filter_class = commentsFilter


class commentDetailView(generics.RetrieveUpdateDestroyAPIView) :
    model = Comment
    serializer_class = CommentDetailSerializer




class PhoneNumbersFilter(django_filters.FilterSet):
    class Meta:
        model = PhoneNumber
        fields = ['clinic']


class PhoneNumberListView(generics.ListCreateAPIView):
    model = PhoneNumber
    serializer_class = PhoneNumberSerializer
    filter_class = PhoneNumbersFilter

class PhoneNumberDetailView(generics.RetrieveUpdateDestroyAPIView) :
    model = PhoneNumber
    serializer_class = PhoneNumberSerializer








class PicturesFilter(django_filters.FilterSet):
    class Meta:
        model = Picture
        fields = ['clinic']


class PicturesListView(generics.ListCreateAPIView):
    model = Picture
    serializer_class = PicturesSerializer
    filter_class = PicturesFilter


class PicturesDetailView(generics.RetrieveUpdateDestroyAPIView) :
    model = Picture
    serializer_class = PicturesSerializer



class OperatingHoursFilter(django_filters.FilterSet):
    class Meta:
        model = OperatingHours
        fields = ['clinic']


class OperatingHoursListView(generics.ListCreateAPIView):
    model = OperatingHours
    serializer_class = OperatingHoursSerializer
    filter_class = OperatingHoursFilter


class OperatingHoursDetailView(generics.RetrieveUpdateDestroyAPIView) :
    model = OperatingHours
    serializer_class = OperatingHoursSerializer




class InsurancesFilter(django_filters.FilterSet):
    class Meta:
        model = Insurance
        fields = ['clinic']


class InsurancesListView(generics.ListCreateAPIView):
    model = Insurance
    serializer_class = InsurancesSerializer
    filter_class = InsurancesFilter


class InsurancesDetailView(generics.RetrieveUpdateDestroyAPIView) :
    model = Insurance
    serializer_class = InsurancesSerializer


