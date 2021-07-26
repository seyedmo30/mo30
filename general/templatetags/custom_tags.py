from django import template
from django.conf import settings
import os.path
register = template.Library()
    
    
@register.simple_tag
def halfNumber(value):
      return (value * 0.5)
register.filter('halfNumber', halfNumber)
          
@register.simple_tag
def slashToBash(value):
      value = value.replace(".","-")
      return  value.replace("/","-")
register.filter('slashToBash', slashToBash)
      
@register.simple_tag
def returnDirImg( **kwargs):
      name = kwargs.get('name')
      singer = kwargs.get('singer')
      albumimg = kwargs.get('albumimg')
      if albumimg != 'None' :            
            if os.path.isfile(str(settings.MEDIA_ROOT) + "img/albums/webp/" + str(name)+".webp"):
                  return  "/media/img/albums/webp/"+name+".webp"
            else:
                  return  "/media/"+str(albumimg)
      else:
            return  "/media/"+str(singer)