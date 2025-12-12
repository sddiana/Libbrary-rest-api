from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import viewsets

def home_view(request):
    return HttpResponse("Добро пожаловать на главную страницу!")


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
