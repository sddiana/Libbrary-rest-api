from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    #Сериализатор для книг с детальной информацией об авторе
    author = AuthorSerializer(read_only=True)  # Вложенная информация об авторе
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True,
        required=True
    )
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_id', 'publication_year', 'genre', 'publisher', 'category', 'cover_image', 'book_file',
        ]
        #read_only_fields = ['created_at']