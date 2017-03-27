from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'app': 'quora'}
    return render(request, 'apps/quora/quora.html', {'context': context})