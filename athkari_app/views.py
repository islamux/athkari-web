from django.shortcuts import render
from .models import Athkar

def home(request):
    athkar_list = Athkar.objects.all()
    return render(request, 'index.html', {'athkar_list': athkar_list})

def athkar_detail(request, athkar_id):
    athkar = Athkar.objects.get(id=athkar_id)
    return render(request, 'athkar_detail.html', {'athkar': athkar})

def athkar_massa(request):
    return render(request, 'athkar_massa.html')

def athkar_sabah(request):
    return render(request, 'athkar_sabah.html')
