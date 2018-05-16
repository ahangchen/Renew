from django.db import models

# Create your models here.
from word2vec.profile.defines import SHORT_TEXT_LENGTH


class Usr(models.Model):
    mail = models.CharField(max_length=SHORT_TEXT_LENGTH, default='cweihang@foxmail.com')


class Word(models.Model):
    word = models.CharField(max_length=SHORT_TEXT_LENGTH)
    meaning = models.CharField(max_length=SHORT_TEXT_LENGTH)
    review_cnt = models.IntegerField(default=0)
    user = models.ForeignKey(Usr, on_delete=models.SET_NULL, null=True)

