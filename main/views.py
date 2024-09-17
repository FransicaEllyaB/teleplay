from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import VideoForm
from main.models import Video

def show_main(request):
    video_entries = Video.objects.all()

    context = {
        'app_name' : 'Teleplay',
        'name' : 'Fransisca Ellya Bunaren',
        'class' : 'PBP F',
        'video_entries': video_entries
    }

    return render(request, "main.html", context)

def create_video_entry(request):
    form = VideoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_video_entry.html", context)

def show_xml(request):
    data = Video.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Video.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Video.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Video.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")