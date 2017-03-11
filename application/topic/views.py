from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'app': 'topic'}
    return render(request, 'apps/topic.html', {'context': context})