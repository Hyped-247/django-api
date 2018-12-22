from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^status/api/', include('status.api.urls', namespace='status')),
    url(r'^author/api/', include('authors.api.urls', namespace='author'))
    
    # path('json/JsonCBV/', JsonCBV.as_view()),
    # path('json/JsonCBV2/', JsonCBV2.as_view()),
    # path('json/SerializedView/', SerializedView.as_view()),
    # path('json/SerializedDetail/', SerializedDetail.as_view()),
]
