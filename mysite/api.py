
from tastypie.resources import ModelResource
from mysite.models import Tweets
from tastypie.constants import ALL

class EntryResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Tweets.objects.all()
        filtering = {'id': ALL}
        resource_name = 'tweet'

