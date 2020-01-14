from django.conf.urls import url
from .views import EntitiesView, EntitiesDetailView

urlpatterns = [
    url(r'^entities/$', EntitiesView.as_view(), name='public_all'),
    url(r'^entities/(?P<slug>[-_\a-z]+)/$', EntitiesDetailView.as_view(), name='public_entity'),
]
