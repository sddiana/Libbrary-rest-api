from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    """
    Модель для представления автора книги.
    """
    #Обязательные поля
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    # Биография (необязательное поле)
    biography = models.TextField(blank=True, null=True)
    
    # Дата рождения (необязательное)
    date_of_birth = models.DateField(blank=True, null=True)
    
    # Дата смерти (необязательное, для умерших авторов)
    date_of_death = models.DateField(blank=True, null=True)

    class Meta:
        #Метаданные модели
        ordering = ['last_name', 'first_name']

    def __str__(self):
        #Строковое представление объекта (для админки и shell)
        return f'{self.last_name} {self.first_name}'
    
class Book(models.Model):
    """
    Модель для представления книги в электронной библиотеке.
    """
    # 1. Название книги (строка, максимум 100 символов)
    title = models.CharField(max_length=100)
    
    # 2. Автор книги (внешний ключ на таблицу авторов)
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        related_name='books'
    )
    
    # 3. Год выпуска (целое число от 1000 до 9999)
    publication_year = models.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    
    # 4. Жанр книги (строка, максимум 100 символов)
    genre = models.CharField(max_length=100)
    
    # 5. Категория книги (строка, максимум 100 символов)
    category = models.CharField(max_length=100)
    
    # 6. Издательство (строка, максимум 100 символов)
    publisher = models.CharField(max_length=100)
    
    # 7. Изображение обложки книги
    cover_image = models.ImageField(
        upload_to='book_covers/',
        blank=True,
        null=True
    )
    
    # 8. Файл с текстом книги
    book_file = models.FileField(
        upload_to='book_files/',
        blank=True,
        null=True
    )

    class Meta:
        # Уникальность по сочетанию полей
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author', 'publication_year', 'publisher'],
                name='unique_book_entry'
            )
        ]
        
        # Сортировка по умолчанию
        ordering = ['title', 'author']

    def __str__(self):
        #Строковое представление книги.
        return f'{self.title} ({self.author}, {self.publication_year})'