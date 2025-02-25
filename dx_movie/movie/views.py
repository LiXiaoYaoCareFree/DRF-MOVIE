# 导入了 Movie 和 Category 模型，这些模型定义了电影和电影分类的信息。
from movie.models import Movie, Category
# 导入了序列化器，用于将模型数据转换为 JSON 格式，或将 JSON 数据转换回模型实例。
from movie.serializers import MovieSerializer, CategorySerializer
# 导入 Django REST framework 的通用视图类，虽然这里注释掉了，但它提供了常用的视图（如 ListCreateAPIView 和 RetrieveUpdateDestroyAPIView）来处理 CRUD 操作。
from rest_framework import generics
# 导入 Django-filter 的后台过滤器，用于处理基于字段的过滤。
from django_filters.rest_framework import DjangoFilterBackend
# 导入自定义的分页类，帮助处理分页逻辑。
from utils.pagination import CustomPagination
# 导入自定义的过滤器，用于对电影数据进行过滤。
from .movie_filters import MovieFilter
# 导入视图集类，提供标准的 CRUD 操作接口。
from rest_framework import viewsets
# 导入 Django-filter 的模块，用于过滤器类的定义。
from django_filters import rest_framework as filters
# 导入权限类，用于限制权限。
from rest_framework.permissions import IsAdminUser
# 导入 Response 类，用于返回响应。
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
# 
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
# MovieFilter 类使用 Django-filter 来定义过滤条件，可以对电影的名称、类别 ID 和地区进行过滤：
class MovieFilter(filters.FilterSet):
    # 允许用户基于电影名称模糊搜索（忽略大小写）。
    movie_name = filters.CharFilter(lookup_expr='icontains')
    # 允许基于分类 ID 进行精确过滤。
    category_id = filters.NumberFilter()
    # 允许基于地区 ID 进行精确过滤。
    region = filters.NumberFilter()

    class Meta:
        model = Movie
        fields = ['movie_name', 'category_id', 'region']
# MovieViewSet 是一个 ModelViewSet 类，提供了对 Movie 模型的 CRUD 操作（增删改查）接口：
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    permission_classes = [IsAdminUserOrReadOnly]
 # CategoryViewSet 也是一个 ModelViewSet 类，提供了对 Category 模型的 CRUD 操作接口：   
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]




