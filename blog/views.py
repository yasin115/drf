from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer,UserSerializer
from rest_framework import viewsets
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permission import IsOwnerOrReadOnly,IsUserOrStaff
from rest_framework import permissions


from rest_framework import permissions

class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return super().get_permissions()
class UserView(viewsets.ModelViewSet):
    queryset =User.objects.all()
    permission_classes = [IsUserOrStaff]
    serializer_class = UserSerializer