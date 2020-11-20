import django_filters
from api.models import Entity


class TagFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(
        field_name='tags__name',
        lookup_expr='exact'
    )

    class Meta:
        model = Entity
        fields = ('tags',)
