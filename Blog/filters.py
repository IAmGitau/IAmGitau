from django_filters import FilterSet
from .models import Blog


class ArticleFilter(FilterSet):
    class Meta:
        model = Blog
        fields = ('Title', 'slug', 'Body',)
