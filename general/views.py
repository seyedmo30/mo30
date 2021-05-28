from django.shortcuts import render , redirect
from .models import Music , Artist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from profiles.models import Rate
from django.db.models import Q ,F , OuterRef, Subquery

from django.http import HttpResponse, JsonResponse
from decimal import Decimal
from django.db.models import IntegerField, Value , BooleanField


def googleVerify(request):
    return render(request,'google230e3cfee612c87e.html',{})

def paginator_and_return(request,total_musics,*args,**kwargs):
    singers=Artist.objects.filter(main_art=0)
    paginator  = Paginator(total_musics, 21)
    page = request.GET.get('page', 1)
    try:
        musics = paginator.page(page)
    except PageNotAnInteger:
        musics = paginator.page(1)
    except EmptyPage:
        musics = paginator.page(paginator.num_pages)
    context = {
        "musics" : musics,
        "singers":singers,
    }
    return context

def index(request,*args,**kwargs):

    if request.user.is_authenticated:
        rate_user = Rate.objects.filter(user_r=request.user).filter(music_r=OuterRef('pk'))
        total_musics = Music.objects.all().annotate(rate=Subquery(rate_user.values("rate_r")) , like =Subquery(rate_user.values("like_r")) ).values('id','avg_rate','album__name','file_name','singer__img','name','rate','album__img','like').order_by('-avg_rate')
    else:
        total_musics = Music.objects.all().values('id','avg_rate','album__name','file_name','singer__img','name','album__img').order_by('-avg_rate')

    context =paginator_and_return(request,total_musics)
        
    context["title"]= " ابی -هایده - داریوش - سیاوش قمیشی"

    context["description"]= "برترین آهنگ های ستارگان دهه شصت به انتخاب شما - ابی هایده داریوش سیاوش" 

    return render(request,'index.html',context)

def myBest(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('/')
    musics_rated = Music.objects.filter(Q(music_rate__user_r=request.user) & Q(music_rate__rate_r__isnull=False)).annotate(rate=F("music_rate__rate_r") , like =F("music_rate__like_r") ).values('id','avg_rate','album__name','file_name','singer__img','name','rate','album__img','album__img','like').order_by('-rate')
    total_musics =musics_rated 
    context =paginator_and_return(request,total_musics)
    
    context["title"]= "بالا ترین رتبه ها"

    context["description"]= "- برترن رتبه های شما" 

    return render(request,'index.html',context)

def myFavorite(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('/')
    musics_rated = Music.objects.filter(Q(music_rate__user_r=request.user) & Q(music_rate__like_r=True)).annotate(rate=F("music_rate__rate_r") , like =F("music_rate__like_r") ).values('id','avg_rate','album__name','file_name','singer__img','name','rate','album__img','album__img','like').order_by('-rate')
    total_musics =musics_rated 
    context =paginator_and_return(request,total_musics)
    
    context["title"]= "مورد علاقه"

    context["description"]= "- آهنگ های مورد علاقه به انتخاب شما" 

    return render(request,'index.html',context)

def news(request,*args,**kwargs):
    if not request.user.is_authenticated:
        return redirect('/')
    total_musics = Music.objects.exclude(music_rate__user_r=request.user).values('id','avg_rate','album__name','file_name','singer__img','name','album__img','album__img').order_by('-avg_rate')
    context =paginator_and_return(request,total_musics)

    context["title"]= "مشاهده نشده"

    context["description"]= "- به این آهنگ ها هنوز رتبه نداده اید" 

    return render(request,'index.html',context)
 
def artists(request,*args,**kwargs):


    if request.user.is_authenticated:
        rate_user = Rate.objects.filter(user_r=request.user).filter(music_r=OuterRef('pk'))
        total_musics = Music.objects.filter(singer__slug=(kwargs)['slug']).annotate(rate=Subquery(rate_user.values("rate_r")) , like =Subquery(rate_user.values("like_r")) ).values('id','avg_rate','album__name','file_name','singer__img','name','rate','album__img','like').order_by('-avg_rate')
    else:
        total_musics = Music.objects.filter(singer__slug=(kwargs)['slug']).values('id','avg_rate','album__name','file_name','singer__img','name','album__img').order_by('-avg_rate')

    context =paginator_and_return(request,total_musics)
    artist = str(Artist.objects.get(slug=(kwargs)['slug']))
    context["title"]= artist + " - " + str((kwargs)['slug'])

    context["description"]= artist 


    return render(request,'index.html',context)

def music(request,*args,**kwargs):
    
    value = (kwargs)['slug'].replace("-","/")
    value = value.replace("/mp3",".mp3")

    music = Music.objects.select_related('singer').select_related('album').get(file_name=value)

    context = {
        "music" : music,
        # "singers":singers,
    }
    title = []

    try:
        title.append(music.singer.slug)
        title.append(music.singer.name)
    except:
        pass

    try:
        title.append(music.album.slug)
        title.append(music.album.name)
    except:
        pass

    string = " - "
    string = string.join(title)
    context["title"]=  str(music.name) + " | " + string 

    context["description"]= "برترین آهنگ های ستارگان دهه شصت به انتخاب شما - ابی هایده داریوش سیاوش"  + string

    return render(request,'detail.html',context)

def detail(request,*args,**kwargs):
    from django.conf import settings
    import os    
    import shutil
    base_dir = settings.BASE_DIR
    backup = shutil.make_archive(os.path.join(base_dir, 'public/backup'), 'zip', base_dir, 'db.sqlite3')
    if os.path.exists(backup):
        with open(backup, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/zip")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(backup)
            return response
    return render(request,'detail.html',{'backup':backup})


def ajaxHeartSubmit(request,*args,**kwargs):
    try:
        id = request.POST.get('id')
        status = request.POST.get('status')
        if status == '1' :
            obj, created =Rate.objects.update_or_create(user_r=request.user,music_r_id=id,defaults={'like_r': True},)
        else:
            obj_r = Rate.objects.get(music_r_id=id)
            if obj_r.rate_r:
                obj, created =Rate.objects.update_or_create(user_r=request.user,music_r_id=id,defaults={'like_r': False},)
            else:
                obj_r.delete()
        return JsonResponse({},status=304)
    except:
        return JsonResponse({'message':'برای ثبت نظر ابتدا وارد حساب شوید'},status=200)


def ajaxStarSubmit(request,*args,**kwargs): 
    try:
        id = request.POST.get('id')
        rate = int(Decimal(request.POST.get('rate')) * 2)

        obj, created =Rate.objects.update_or_create(user_r=request.user,music_r_id=id,defaults={'rate_r': rate},)

        return JsonResponse({},status=304)
    except:
        return JsonResponse({'message':'برای ثبت نظر ابتدا وارد حساب شوید'},status=200)
