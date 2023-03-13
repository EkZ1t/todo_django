from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    completed = models.BooleanField(
        verbose_name='Выполнено-ли',
        default=False
    )
    created_at = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True
    )
    deadline = models.DateTimeField(
        verbose_name='Крайний срок'
    )
    
    def __str__(self):
        return self.title
    
    
# Миграции - система контроля версий таблиц в базе данных 