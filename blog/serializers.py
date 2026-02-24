from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    author = UserSerializer()
    def validate_name(self, value):
        if value == "test" or value == "set":
            raise serializers.ValidationError("Name cannot be " + value)
        return value
    def validate(self, attrs):
        if len(attrs["desc"]) > 3:
            raise serializers.ValidationError("Start date must be before end date")
        return attrs 