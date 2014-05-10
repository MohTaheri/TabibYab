from django.conf.urls import patterns, include, url
from doctorHandler.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib.gis import admin
from django.conf import settings
from django.conf.urls.static import static



admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Doctors.views.home', name='home'),
    # url(r'^Doctors/', include('Doctors.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^search', doctorsListView.as_view() ) ,
    url(r'^doctor/(?P<pk>[0-9]+)/$',doctorDetailView.as_view()) ,

    url(r'^comments',commentListView.as_view() ) ,
    url(r'^comment/(?P<pk>[0-9]+)/$',commentDetailView.as_view()) ,

    url(r'^phonenumbers',PhoneNumberListView.as_view() ) ,
    url(r'^phonenumber/(?P<pk>[0-9]+)/$',PhoneNumberDetailView.as_view()) ,

    url(r'^operatinghours',OperatingHoursListView.as_view() ) ,
    url(r'^operatinghour/(?P<pk>[0-9]+)/$',OperatingHoursDetailView.as_view()) ,

    url(r'^pictures',PicturesListView.as_view() ) ,
    url(r'^picture/(?P<pk>[0-9]+)/$',PicturesDetailView.as_view()) ,

    url(r'^insurances',InsurancesListView.as_view() ) ,
    url(r'^insurance/(?P<pk>[0-9]+)/$',InsurancesDetailView.as_view()) ,
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
