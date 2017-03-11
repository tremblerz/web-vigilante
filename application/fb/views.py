from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'app': 'fb'}
    return render(request, 'apps/fb.html', {'context': context})