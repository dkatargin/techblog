from rest_framework import generics
from .models import Entity
from .serializers import EntitySerializer, EntityDetailSerializer


class EntitiesView(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class EntitiesDetailView(generics.RetrieveAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntityDetailSerializer
    lookup_field = 'slug'
