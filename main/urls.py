from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', include(router.urls)),
]
