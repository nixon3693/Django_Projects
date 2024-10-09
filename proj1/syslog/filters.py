from django_filters import FilterSet
from .models import *


class SyslogFilter(FilterSet):
    class Meta:
        model = SyslogModel
        fields = {
            "datetime": ['icontains'],
            "host": ['icontains'],
            "type": ['icontains'],
        }
