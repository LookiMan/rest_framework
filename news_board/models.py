from django.db import models
from django.db.models.fields import (CharField, PositiveBigIntegerField,
                                     TextField, DateTimeField, URLField)


class Post(models.Model):
    title = CharField(max_length=128, verbose_name='Заголовок')
    url = URLField(verbose_name='URL адрес')
    author = CharField(max_length=128, verbose_name='Автор')
    votes = PositiveBigIntegerField(verbose_name='Голоса', default=0)
    created_at = DateTimeField(
        auto_now_add=True, verbose_name='Время публикации')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('news_board.Post', on_delete=models.PROTECT)
    author = CharField(max_length=128, verbose_name='Автор')
    message = TextField(verbose_name='Коментарий')
    created_at = DateTimeField(
        auto_now_add=True, verbose_name='Время публикации')

    def __str__(self):
        return self.author
