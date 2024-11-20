from django.forms import ModelForm
from django import forms
from main.models import Video
from django.utils.html import strip_tags

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ["name", "price", "description", "duration", "video_thumbnail"]
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : "Enter video's name",
                                     'required': 'required'}),
            'duration' : forms.TimeInput(format='%H:%M:%S', attrs={'placeholder' : "HH:MM:SS"}),
        }
    
    def clean_name(self):
        video = self.cleaned_data["name"]
        return strip_tags(video)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    @property
    def valid_thumbnail(self):
        if not self.video_thumbnail or not self.video_thumbnail.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return ""
        return self.video_thumbnail