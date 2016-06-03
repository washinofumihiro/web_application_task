from django.db import models


class Book(models.Model):
    """書籍"""
    name = models.CharField('タイトル', max_length=255)
    publisher = models.TextField('内容', blank=True)
    # publisher = models.CharField('出版社', max_length=255, blank=True)
    # page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name

#
# class Impression(models.Model):
#     """感想"""
#     book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions')
#     comment = models.TextField('コメント', blank=True)
#
#     def __str__(self):
#         return self.comment

class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions')
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

