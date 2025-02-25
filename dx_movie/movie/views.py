from movie.models import Movie, Category
# 导入了序列化器，用于将模型数据转换为 JSON 格式，或将 JSON 数据转换回模型实例。
from movie.serializers import MovieSerializer, CategorySerializer
# 导入 Django REST framework 的通用视图类，虽然这里注释掉了，但它提供了常用的视图（如 ListCreateAPIView 和 RetrieveUpdateDestroyAPIView）来处理 CRUD 操作。
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from utils.pagination import CustomPagination
from .movie_filters import MovieFilter


from rest_framework import viewsets
from django_filters import rest_framework as filters

from rest_framework.permissions import IsAdminUser

from rest_framework.response import Response

# class MovieList(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)  
#     filterset_class = MovieFilter
#     pagination_class = CustomPagination


# class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieDetailSerializer


# class Category(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    仅管理员用户可进行修改
    其他用户仅可查看
    """
    def has_permission(self, request, view):
        # 对所有人允许 GET, HEAD, OPTIONS 请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 仅管理员可进行其他操作
        return request.user.is_superuser

class MovieFilter(filters.FilterSet):
    movie_name = filters.CharFilter(lookup_expr='icontains')
    category_id = filters.NumberFilter()
    region = filters.NumberFilter()

    class Meta:
        model = Movie
        fields = ['movie_name', 'category_id', 'region']

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [IsAdminUserOrReadOnly]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]




