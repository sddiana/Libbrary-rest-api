from django.http import HttpResponse
from .models import Author, Book
from .serializers import AuthorSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from .filters import BookFilter

def home_view(request):
    return HttpResponse("Добро пожаловать на главную страницу!")

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Настройка фильтрации и поиска
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Для django-filter
    filterset_class = BookFilter
    
    # Для SearchFilter 
    search_fields = ['title', 'genre', 'author__last_name', 'author__first_name']
    
    # Поля для сортировки
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  

    def get_queryset(self):
        """
        Дополнительная оптимизация: предзагрузка связанных данных.
        """
        queryset = super().get_queryset()
        # Оптимизация: загружаем автора одним запросом (avoid N+1 problem)
        queryset = queryset.select_related('author')
        return queryset
