from django.db import models
from models import TimestampModel


class Category(models.Model):
    name = models.CharField(max_length=25)
    parents = models.ForeignKey('board.Category', on_delete=models.CASCADE,
                                related_name='category_parents', blank=True, null=True)

    class Meta:
        db_table = 'categories'


class Board(TimestampModel):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=225)
    content = models.CharField(max_length=1000)
    category = models.ForeignKey('board.Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'boards'


class Comment(TimestampModel):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=225)
    reply = models.CharField(max_length=255)
    board = models.ForeignKey('board.Board', on_delete=models.CASCADE)
    parents = models.ForeignKey('board.Comment', on_delete=models.CASCADE,
                                related_name='comment_parents', null=True, blank=True)

    class Meta:
        db_table = 'comments'
