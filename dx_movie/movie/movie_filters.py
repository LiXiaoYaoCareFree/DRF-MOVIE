import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    movie_name = django_filters.CharFilter(lookup_expr='icontains')
    category_id = django_filters.NumberFilter()
    region = django_filters.NumberFilter()

    class Meta:
        model = Movie
        fields = ['movie_name', 'category_id', 'region']
