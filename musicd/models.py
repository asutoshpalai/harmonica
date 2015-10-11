from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, blank=True)
    uploaded = models.FileField()

    def __str__(self):
        return self.title + ' - ' + self.artist
