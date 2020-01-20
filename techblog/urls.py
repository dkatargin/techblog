from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path
from api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(api_urls)),
    path('summernote/', include('django_summernote.urls')),
]
