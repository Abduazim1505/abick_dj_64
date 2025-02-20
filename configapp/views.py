from django.shortcuts import render
from .models import *


def index(request):
    salon = AutoSalon.objects.all()

    context = {
        "salon": salon,
        "title": "Village autosaloni"
    }

    return render(request, 'AutoSalon/index.html', context=context)