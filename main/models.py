from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    task = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
