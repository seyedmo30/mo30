from django.db import models
from django.contrib.auth.models import AbstractUser
from index.settings import AUTH_USER_MODEL as User
from general.models import Music

class CustomUser(AbstractUser):

    img_user = models.ImageField(upload_to='img/profiles/', null=True, blank=True)
    phone_user = models.CharField(max_length=14, null=True, blank=True)

class Rate(models.Model):
    rate_r=models.PositiveIntegerField(blank=True,null=True)
    like_r=models.BooleanField(default=False)
    user_r=models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_rates')
    music_r=models.ForeignKey(Music ,on_delete=models.CASCADE, related_name='music_rates',related_query_name='music_rate')

    class Meta:
        index_together = (('user_r','music_r'),)



class Feedback (models.Model):
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_send', null=True, blank=True)
    comment = models.CharField(max_length=300)

