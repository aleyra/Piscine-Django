from django.db import models

# Create your models here.

# https://docs.djangoproject.com/fr/5.0/ref/contrib/postgres/fields/

class Movies(models.Model):
    class Meta:
        db_table = 'ex05_movies'
    title = models.CharField(max_length=64, unique=True)  # VARCHAR(64) NOT NULL UNIQUE,
    episode_nb = models.IntegerField(primary_key=True)  # INTEGER PRIMARY KEY,
    opening_crawl = models.TextField(null=True)  # TEXT,
    director = models.CharField(max_length=32)  # VARCHAR(32) NOT NULL,
    producer = models.CharField(max_length=128)  # VARCHAR(128) NOT NULL,
    release_date = models.DateField() # date DATE NOT NULL

    def __str__(self) -> str:
        return self.title