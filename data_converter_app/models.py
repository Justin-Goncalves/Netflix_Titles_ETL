from django.db import models

# Create your models here.


class StreamingContent(models.Model):
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=250)
    cast = models.JSONField(default=list, blank=True)
    country = models.CharField(max_length=200, blank=True)
    date_added = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=10)
    duration = models.CharField(max_length=50)
    listed_in = models.JSONField(default=list, blank=True)
    description = models.CharField(max_length=300)
    
    