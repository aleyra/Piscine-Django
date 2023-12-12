from django.db import models


# https://docs.djangoproject.com/fr/5.0/ref/contrib/postgres/fields/

class movies(models.Model):
    title = models.CharField(max_length=64, null=False, unique=True)  # VARCHAR(64) NOT NULL UNIQUE,
    episode_nb = models.IntegerField(primary_key=True)  # INTEGER PRIMARY KEY,
    opening_crawl = models.TextField(null=True)  # TEXT,
    director = models.CharField(max_length=32, null=False)  # VARCHAR(32) NOT NULL,
    producer = models.CharField(max_length=128, null=False)  # VARCHAR(128) NOT NULL,
    release = models.DateField(null=False) # date DATE NOT NULL

    def __str__(self) -> str:
        return self.title