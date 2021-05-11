from django import template
register = template.Library()
    
    
@register.simple_tag
def halfNumber(value):
      return (value * 0.5)
register.filter('halfNumber', halfNumber)
      