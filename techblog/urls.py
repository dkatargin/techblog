from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path
from api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/blog/', admin.site.urls),
    url('api/blog/rest/', include(api_urls)),
    path('api/blog/summernote/', include('django_summernote.urls')),
]
