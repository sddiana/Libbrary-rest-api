from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', include(router.urls)),
]
