from django.test import TestCase, Client
from datetime import timedelta, datetime
from .models import Video

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_good_movie(self):
        now = datetime.now() 
        video = Video.objects.create(
          name ="Spongebob Ovalpants",
          price = 50000,
          description = "Perjalanan Spongebob Sepanjang Hidupnya",
          release_date = now,
          duration = timedelta(minutes=120),
          rating = 8
        )
        self.assertTrue(video.is_movie_good)