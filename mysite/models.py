from django.db import models
import string



class Tweet(models.Model):
    user = models.BigIntegerField()
    tid = models.BigIntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    text = models.TextField(max_length=256)
    time = models.DateField()
    kwd = models.CharField(max_length=50)

class Tweets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    longitude = models.CharField(max_length=255, blank=True)
    latitude = models.CharField(max_length=255, blank=True)
    tweet_date = models.CharField(max_length=255, blank=True)
    tweet_time = models.CharField(max_length=255, blank=True)
    user_id = models.CharField(max_length=255, blank=True)
    user_location = models.CharField(max_length=255, blank=True)
    user_lang = models.CharField(max_length=255, blank=True)
    text_id = models.CharField(max_length=255, blank=True)
    text_msg = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tweets'

class Grids(models.Model):
    id_grid = models.IntegerField(primary_key=True)
    lat_ini = models.FloatField(blank=True, null=True)
    lat_fin = models.FloatField(blank=True, null=True)
    long_ini = models.FloatField(blank=True, null=True)
    long_fin = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grids'

class UserTweets(models.Model):
    id = models.TextField(primary_key=True)
    number = models.TextField(blank=True)
    n = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tweets'
        
class TwTabTime(models.Model):
    id_time = models.IntegerField(primary_key=True)
    lapso = models.CharField(max_length=30)
    cantidad_twts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tw_tab_time'
