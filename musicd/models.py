from django.db import models
from django.contrib.auth.models import User

class Track(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, blank=True)
    uploaded = models.FileField()

    def rate(self):
        sum = 0
        count = 0
        for v in self.vote_set.all():
            sum += v.vote
            count += 1

        return sum/(count if (count != 0) else 1)



    def __str__(self):
        return self.title + ' - ' + self.artist

class Vote(models.Model):

    class Meta:
        unique_together = (('track', 'user'),)
    VOTES = ( (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    track = models.ForeignKey(Track)
    user = models.ForeignKey(User)
    vote = models.IntegerField(choices=VOTES)

