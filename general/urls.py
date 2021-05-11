from .views import *
from django.urls import path 
app_name = 'rate'
urlpatterns = [
    path('ajax-heart-submit/', ajaxHeartSubmit, name='ajax-heart-submit'),

    path('ajax-star-submit/', ajaxStarSubmit, name='ajax-star-submit'),
 
 
]
 