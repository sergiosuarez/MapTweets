# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render
from mysite.models import Tweet
from mysite.models import Tweets,Grids
from mysite.models import UserTweets,TwTabTime

#from twittmap.models import convertstof
from django.http import HttpResponse
from django.core.context_processors import request
from datetime import datetime, timedelta, date
import simplejson as json
import tweepy
import django.db as jdb
from tweepy.utils import import_simplejson

import twitter
import os
import json
import codecs
def getData(request):
    from django.core import serializers
    query = {}
    if request.method == 'GET':
        type = request.GET.get('type',None)
        if type:
            if type == '1':
                query = Tweets.objects.all()
            elif type == '2':
                query = Grids.objects.all()
            elif type == '3':
                query = UserTweets.objects.all()
            elif type == '4':
                query = TwTabTime.objects.all()
        return HttpResponse(serializers.serialize('json', query))

def index(request):
    twets = Tweets.objects.all()
    bbs = Grids.objects.all()
    context = {
            'twets': twets,
            'bbs': bbs,
            }
     #return HttpResponse('Templates/index.html',locals(),context_instance = RequestContext(request))
    return render(request, 'static/index.html', context)




def search_twitter(data, kkwd):

    #filter it all
#     print data
    tweets = []
    try:

            user = data.id
            tid = data.user.id
            geo = data.coordinates
            text = data.text
            ts = data.created_at
            time = data.created_at#datetime.strptime(data.created_at,'%a %b %d %H:%M:%S +0000 %Y')

    except AttributeError:
        return

    if geo is not None and text is not None and tid is not None and time is not None and user is not None:

        try:
            p = Tweet(
                      user = data.id,
                      tid = data.user.id,
                      lat = data.coordinates['coordinates'][0],
                      lon = data.coordinates['coordinates'][1],
                      text = data.text,
                      time = data.created_at,#datetime.strptime(data.created_at,'%a %b %d %H:%M:%S +0000 %Y'),
                      kwd = kkwd,
                      )
            p.save()
        except jdb.OperationalError:
            return

def crawl(request):

    CONSUMER_KEY = 'KIk4y0OV3zjX0aTfDRg4yZyYy'
    CONSUMER_SECRET = 'c4XG4cMOthUNVIEbWiU7WZsAl2hjO1Az24GUUg2FlDStZeTvmS'
    ACCESS_TOKEN_KEY = '19185688-50H5C08Lu9cYvZD6RaODx1qbCU7B99I8pg6KDNYuu'
    ACCESS_TOKEN_SECRET = 'LST0w66qpbRFgKgiaFBBD93iqBcqIfE8FEQLHx94jZMdV'

    kkwd = request.GET.get('kwd');

    auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth1.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)


    api = tweepy.API(auth1)
    data = api.search(q=kkwd, lang='en', count=100)
    print data
    for d in data:
        search_twitter(d, kkwd)

    return HttpResponse('Done!')

