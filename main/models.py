import uuid
from django.db import models

class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    @property
    def is_movie_good(self):
        return self.rating > 7