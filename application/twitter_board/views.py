from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {'app': 'twitter'}
    return render(request, 'apps/twitter.html', {'context': context})