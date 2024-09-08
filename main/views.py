from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Teleplay',
        'name' : 'Fransisca Ellya Bunaren',
        'class' : 'PBP F'
    }

    return render(request, "main.html", context)