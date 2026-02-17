from django.urls import path
from .views import ArticleList,ArticleShow,UserList,UserShow
urlpatterns = [
    path('',ArticleList.as_view()),
    path('<int:pk>',ArticleShow.as_view()),
    path('user/',UserList.as_view()),
    path('user/<int:pk>',UserShow.as_view()),
]