import django_filters
from .models import *
from django_filters import DateFilter, CharFilter

class NewsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="time_added", lookup_expr='gte')
    end_date = DateFilter(field_name="time_added", lookup_expr='lte')
    name = CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model = News
        fields = ['name']

