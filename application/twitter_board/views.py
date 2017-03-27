from django.shortcuts import render
from django.http import HttpResponse
from .models import TweetData, TwitterUser
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    context = {'app': 'twitter'}
    return render(request, 'apps/twitter/twitter.html', {'context': context})

def get_tweet(request):
    if request.method == "POST":
        if 'sentiment' in request.POST.keys() and 'index' in request.POST.keys():
            if request.POST['sentiment'] and request.POST['index']:
                sentiment = request.POST['sentiment']
                index = int(request.POST['index'])
                if sentiment == 'pos':
                    tweet = TweetData.objects.filter(polarity__gt = 0)[index]
                elif sentiment == 'neg':
                    tweet = TweetData.objects.filter(polarity__lt = 0)[index]

                tweet_data = {
                            'tweet': tweet.tweet_id,
                            'tweet': tweet.tweet,
                            'polarity': float(tweet.polarity),
                            'subjectivity': float(tweet.subjectivity),
                            'favourite_count': tweet.favourite_count,
                            'user_name': tweet.user.user_name,
                            'user_profile_image_url': tweet.user.user_profile_image_url,
                            'user_followers': tweet.user.user_followers
                        }

                tweet = json.dumps(tweet_data)
                return HttpResponse(tweet, content_type = 'application/json')
            else:
                return HttpResponse("arguments are not defined")
        else:
            return HttpResponse("sentiment and index is necessary argument")
    else:
        return HttpResponse("Only POST request is accepted")
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def get_realtime_polarity(request):
    if request.method == "POST":
        if 'index' in request.POST.keys():
            if request.POST['index']:
                index = int(request.POST['index'])
                polarity = TweetData.objects.all()[index].polarity
                data = json.dumps({'polarity': float(polarity)})
                return HttpResponse(data, content_type='application/json')
            else:
                return HttpResponse("arguments are not defined")
        else:
            return HttpResponse("index is necessary argument")
    else:
        return HttpResponse("Only POST request is accepted")