# Create your views here.
import django_filters
from forms import *
from models import *
from rest_framework import generics
from serializers import *
from decimal import *
from django.contrib.gis.geos import *
from django.db.models import Q
from django import db
import operator


# def search_view(request):
#
#     model = Clinic
#     initial_queryset = model.objects.all()
#     form = searchForm(request.GET)
#     predicates = []
#     if form.is_valid() :
#         for fieldname in form.fields:
#             print fieldname
#             print type(form.cleaned_data[fieldname])
#
#         predicates += [('name'+'__contains',form.cleaned_data['name'])]
#         if predicates != [] :
#             q_list = [Q(x) for x in predicates]
#             initial_queryset = initial_queryset.filter(reduce(operator.and_,q_list))


class doctorsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='contains')
    class Meta:
        model = Clinic
        fields = ['name']


class doctorsListView(generics.ListCreateAPIView):
    model = Clinic
    serializer_class = ClinicListSerializer
    filter_class = doctorsFilter

    def get_queryset(self):

        query_set = Clinic.objects.all()
        if self.request.GET.__contains__('lat') and self.request.GET.__contains__('long'):
            lat = self.request.GET['lat']
            long = self.request.GET['long']
            pnt = fromstr('POINT('+lat+' ' +long+')', srid=4326)
            query_set = query_set.filter(coordinates__distance_lte=(pnt, 10))

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