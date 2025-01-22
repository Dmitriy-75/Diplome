from django.db import models
from slugify import slugify


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)  # Название задачи
    content = models.TextField(blank=True)  # Содержание задачи
    priority = models.PositiveIntegerField()  # Приоритет задачи
    completed = models.BooleanField()  # Исполнение задачи
    user_id = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)  # Привязка к пользователю
    slug = models.SlugField(blank=True)  # lug названия задачи

    def save(self, *args, **kwargs):
        """получение slug из title"""
        if not self.id:
            self.slug = slugify(self.str(title))
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'  # Строковое представление объекта


class User(models.Model):
    firstname = models.CharField(max_length=40)  # Имя пользователя
    lastname = models.CharField(max_length=40)  # Фамилия пользователя
    email = models.EmailField(unique=True)  # Уникальный email пользователя
    age = models.PositiveIntegerField()  # Возраст
    job = models.CharField(max_length=40, default="Безработный(ая)")  # Профессия

    def __str__(self):
        return f'{self.firstname} {self.lastname}'  # Строковое представление объекта
