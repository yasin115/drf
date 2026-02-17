from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer,UserSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permission import IsOwnerOrReadOnly,IsUserOrStaff
class ArticleList(ListCreateAPIView):
    queryset =Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleShow(RetrieveUpdateDestroyAPIView):
    queryset =Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer
class UserList(ListCreateAPIView):
    queryset =User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrStaff]
class UserShow(RetrieveUpdateDestroyAPIView):
    queryset =User.objects.all()
    permission_classes = [IsUserOrStaff]

    serializer_class = UserSerializer