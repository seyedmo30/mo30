from django import template
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
      