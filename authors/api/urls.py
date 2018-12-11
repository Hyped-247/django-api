from django.conf.urls import url
from .views import (ListCreateModelAuthorAPI,
                    DetailUpdateDeleteModelAuthorAPI)

app_name = 'authors'

urlpatterns = [
   url('^$', ListCreateModelAuthorAPI.as_view()),
   url('^(?P<pk>\d+)/$', DetailUpdateDeleteModelAuthorAPI.as_view()),
]
