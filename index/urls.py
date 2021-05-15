
from django.contrib import admin
from django.urls import path , include
from general.views import *
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('detail/<int:pk>', detail),
    path('mybest/', myBest,name="mybest"),
    path('myfavorite/', myFavorite,name="myfavorite"),
    path('news/', news,name="news"),



    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('rate/', include('general.urls', namespace='rate')),
    path('artists/<slug:slug>',artists , name='artists'),

    path('google230e3cfee612c87e', googleVerify),

    path('google230e3cfee612c87e.html', googleVerify),


    path('__debug__/', include(debug_toolbar.urls))

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:


urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
