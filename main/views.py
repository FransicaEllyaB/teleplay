from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import VideoForm
from main.models import Video
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    context = {
        'app_name' : 'Teleplay',
        'name' : request.user.username,
        'npm' : '2306152286',
        'class' : 'PBP F',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_video_entry(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method == "POST":
        video_entry = form.save(commit=False)
        video_entry.user = request.user
        video_entry.save()
        return redirect('main:show_main')

    context = {
        'app_name' : 'Teleplay',
        'form': form
    }
    return render(request, "create_video_entry.html", context)

def show_xml(request):
    data = Video.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Video.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Video.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Video.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
       form = AuthenticationForm(request)
       
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_video(request, id):
    video = Video.objects.get(pk = id)

    form = VideoForm(request.POST or None, request.FILES or None, instance=video)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_video.html", context)

def delete_video(request, id):
    video = Video.objects.get(pk = id)
    video.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_video_entry_ajax(request):
    try:
        name = strip_tags(request.POST.get("name"))
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description"))

        if not name or not price or not description:
            return JsonResponse({"error": "All fields are required."}, status=400)
        
        try:
            price = float(price)
        except ValueError:
            return JsonResponse({"error": "Invalid price format."}, status=400)
        
        try:
            time_parts = list(map(int, request.POST.get("duration").split(':')))
            hours = time_parts[0]
            minutes = time_parts[1]
            seconds = time_parts[2] if len(time_parts) == 3 else 0
            duration = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        except (ValueError, IndexError):
            return JsonResponse({"error": "Invalid duration format."}, status=400)
        
        video_thumbnail = request.FILES.get("video_thumbnail")
        user = request.user

        new_video = Video(
            name = name, price = price,
            description = description, 
            duration = duration,
            video_thumbnail = video_thumbnail,
            user=user
        )
        new_video.save()
        return JsonResponse({"message": "Video created successfully."}, status=201)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)