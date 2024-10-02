import uuid
from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    release_date = models.DateField(auto_now_add=True)
    duration = models.DurationField()
    video_thumbnail = models.ImageField(null=True, blank=True, upload_to="image/")

    @property
    def is_movie_good(self):
        return self.rating > 7