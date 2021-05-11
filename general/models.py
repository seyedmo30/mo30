from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.
class Artist(models.Model):

    MAIN_ART = (
        (0, "خواننده"),
        (1, "آهنگساز"),
        (2, "تنظیم کننده"),
        (3, "شاعر"),
        (4, "غیره"),
        
    )
    
    name = models.CharField(verbose_name='نام - فارسی ', max_length=30)
    description = models.TextField(verbose_name='توصیف ')
    img = models.ImageField(upload_to='img/artists/', null=True, blank=True)
    bg_img = models.ImageField(upload_to='img/background_artists/', null=True, blank=True)
    main_art = models.IntegerField(verbose_name='دسته', choices=MAIN_ART, default=4)
    slug = models.SlugField(verbose_name=' نام - انگلیسی ', max_length=30 , unique=True )
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

class Album(models.Model):
    name = models.CharField(verbose_name='عنوان ', max_length=30)
    description = models.TextField(verbose_name='توصیف ')
    date = models.DateField(verbose_name='تاریخ ',null=True, blank=True)
    img = models.ImageField(upload_to='img/albums/', null=True, blank=True)

    def __str__(self):
        return self.name

def user_directory_path(instance, filename): 
    if instance.album:
        return 'musics/{0}/{1}/{2}'.format(instance.singer.name,instance.album.name ,filename) 
    else:
        return 'musics/{0}/other/{1}'.format(instance.singer.name, filename) 

class Music(models.Model):
    name = models.CharField(verbose_name='عنوان ', max_length=30)
    file_name =models.FileField(upload_to=user_directory_path)
    singer = models.ForeignKey(Artist, verbose_name='singer', related_name='musics_singer', on_delete=models.SET_NULL,null=True)
    composer = models.ForeignKey(Artist, verbose_name='composer', related_name='musics_composer', on_delete=models.SET_NULL,null=True, blank=True)
    arrangement = models.ForeignKey(Artist, verbose_name='arrangement', related_name='musics_arrangement', on_delete=models.SET_NULL,null=True, blank=True)
    poet = models.ForeignKey(Artist, verbose_name='poet', related_name='musics_poet', on_delete=models.SET_NULL,null=True, blank=True)
    album = models.ForeignKey(Album, verbose_name='album', related_name='musics_album', on_delete=models.SET_NULL,null=True, blank=True)
    avg_rate =models.DecimalField(blank=True, null=True,default=15, max_digits=3, decimal_places=1)
    
    def __str__(self):
        return self.name