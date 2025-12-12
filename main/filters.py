import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # Поиск по названию 
    title = django_filters.CharFilter(
        lookup_expr='icontains',  # icontains = содержит
        label='Название книги'
    )
    
    # Поиск по жанру (точное совпадение)
    genre = django_filters.CharFilter(
        lookup_expr='iexact',  # iexact = точное совпадение
        label='Жанр'
    )
    
    # Поиск по фамилии
    author = django_filters.CharFilter(
        field_name='author__last_name',
        lookup_expr='icontains',
        label='Фамилия автора'
    )
    
    # Поиск по имени автора
    author_first_name = django_filters.CharFilter(
        field_name='author__first_name',
        lookup_expr='icontains',
        label='Имя автора'
    )
    
    # Фильтр по году выпуска
    publication_year = django_filters.RangeFilter(
        label='Год выпуска (от-до)'
    )
    
    # Фильтр по типу книги
    category = django_filters.ChoiceFilter(
        choices=Book.CATEGORY_CHOICES,
        label='Тип книги'
    )

    class Meta:
        model = Book
        fields = ['title', 'genre', 'author', 'publication_year', 'category']