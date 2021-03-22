from django_filters import rest_framework as filters

from posts.models import Like


class LikeFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name='timestamp', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = Like
        fields = ['date_from', 'date_to']
