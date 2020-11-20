from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path
from api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/blog/', admin.site.urls),
    url('api/blog/', include(api_urls)),
]
