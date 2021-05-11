from .views import *

from django.urls import path 
app_name = 'profiles'
urlpatterns = [
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
 
    
]
 