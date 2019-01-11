from django.conf.urls import url
from status.api.views import ListCreateModelStatusAPI, DetailUpdateDeleteModelStatusAPI

app_name = 'status'

urlpatterns = [
   url('^$', ListCreateModelStatusAPI.as_view()),
   # url('^create/$', CreateModelStatusAPI.as_view()),
   # url('^detail/(?P<abc>\d+)/$', DetailModelStatusAPI.as_view()),
   url('^(?P<pk>\d+)/$', DetailUpdateDeleteModelStatusAPI.as_view()),
   # url('^update/(?P<pk>\d+)/$', UpdateModelStatusAPI.as_view()),
   # url('^delete/(?P<pk>\d+)/$', DeleteModelStatusAPI.as_view()),
]
