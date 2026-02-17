from rest_framework.serializers import ModelSerializer
from .models import Article
from django.contrib.auth.models import User
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'