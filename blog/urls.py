
from .views import UserView , ArticleView
# urlpatterns = [
#     path('',ArticleList.as_view()),
#     path('<int:pk>',ArticleShow.as_view()),
#     path('user/',UserList.as_view()),
#     path('user/<int:pk>',UserShow.as_view()),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserView, basename='user')
# router.register(r'users', UserShow, basename='users')
# # router.register(r'article', ArticleList, basename='article')
router.register(r'article', ArticleView, basename='article')
urlpatterns = router.urls
