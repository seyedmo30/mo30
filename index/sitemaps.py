from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from general.models import *
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index']
    def location(self, item):
        return reverse(item)

class ArtistSitemap(Sitemap):
    def items(self):
        return Artist.objects.all()

        
class MusicSitemap(Sitemap):
    def items(self):
        return Music.objects.all()

        