from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Users
from . import views

class LatestEntryField(Feed):
    title = " Updates "
    link = "/news-sites/"
    description = "Updates on Users"

    def items(self):
        return Users.objects.order_by ('num')

    def item_title(self, item):
        return item.user

    def item_description(self, item):
        return item.nickname
    #item link is only needed if NewsItem has no get_absolute_url method

    def item_link(self, item):
        return reverse(views.index)
