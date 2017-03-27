from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'app': 'darkweb'}
    return render(request, "apps/darkweb/darkweb.html", {'context': context})