from django.forms import ModelForm
from django import forms
from main.models import Video

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ["name", "price", "description", "duration", "rating"]
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : "Enter video's name"}),
            'duration' : forms.TimeInput(format='%H:%M:%S', attrs={'placeholder' : "HH:MM:SS"}),
        }