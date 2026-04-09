from django.db import models

class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название"
    )
    author = models.CharField(
        max_length=100,
        verbose_name="Автор"
    )
