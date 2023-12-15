from django.db import models
# Create your models here.

class Tip(models.Model):
    class Meta:
        db_table = 'tip'
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)


class Vote(models.Model):
    VOTE = (
        (-1, 'Down vote'),
        (1, 'Up vote'),
    )
    class Meta:
        db_table = 'votes'
    username = models.CharField(max_length=64)
    tip_id = models.IntegerField()
    vote = models.IntegerField(choices=VOTE)