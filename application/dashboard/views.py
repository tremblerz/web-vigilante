from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {'app': 'dashboard'}
    return render(request, 'apps/dashboard/dashboard.html', {'context': context})

def profile(request):
    context = {'app': 'profile'}
    return render(request, 'apps/dashboard/profile.html', {'context': context})

def contrib(request):
    context = {'app': 'contrib'}
    return render(request, 'apps/dashboard/contrib.html', {'context': context})