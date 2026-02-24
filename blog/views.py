from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Article
from .serializers import UserSerializer,ArticleSerializer
from .permission import UserAccessPermission,ArticlePermission

class UserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserAccessPermission]
    


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [ArticlePermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)