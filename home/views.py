from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PhotoFolder
from ratelimit.decorators import ratelimit

# Create your views here.


@ratelimit(key='ip', rate='10/h', block=True)
def home(req):
    photos = PhotoFolder.objects.all().order_by('date').reverse()
    return render(req, 'home/home_index.html', {'photos': photos})


@ratelimit(key='ip', rate='10/h', block=True)
def detail(req):
    photos = PhotoFolder.objects.filter(id=req.POST.get('id'))
    return render(req, 'home/home_detail.html', {'photos': photos})
