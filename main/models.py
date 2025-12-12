from django.db import models

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