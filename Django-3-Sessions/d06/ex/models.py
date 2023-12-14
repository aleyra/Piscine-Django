from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'
    username = models.CharField(max_length=64, unique=True, primary_key=True)
    password = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.username


class Tip(models.Model):
    class Meta:
        db_table = 'tip'
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateField(default=date.today())
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)


class Votes(models.Model):
    VOTE = (
        (-1, 'Down vote'),
        (1, 'Up vote'),
    )
    class Meta:
        db_table = 'votes'
    username = models.CharField(max_length=64)
    tip_id = models.IntegerField()
    vote = models.IntegerField(choices=VOTE)