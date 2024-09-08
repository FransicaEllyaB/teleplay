from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    @property
    def is_movie_good(self):
        return self.rating > 7