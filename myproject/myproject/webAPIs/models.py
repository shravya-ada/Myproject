from django.db import models

# Create your models here.
class Movies(models.Model):
    count = models.IntegerField()
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    genres = models.CharField(max_length=30)
    uuid = models.IntegerField()

    # def __str__(self):
    #     return self.count


class Collection(models.Model):
    collection_title = models.CharField(max_length=20)
    collection_description = models.CharField(max_length=100)
    movie_titles = models.CharField(max_length=200)
    


