import django_filters
from django_filters import DateFilter , CharFilter
from .models import Task


class Orderfilter(django_filters.FilterSet):
    time = DateFilter(field_name = "time" , lookup_expr = 'gte' )
    task = CharFilter(field_name = "task" , lookup_expr = 'icontains')
    class Meta :
        model = Task
        fields = '__all__'
        exclude = ['time' ]