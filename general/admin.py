from django.contrib import admin
from .models import *  
# Register your models here.






from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
	
class FirstModelAdmin(admin.ModelAdmin):
	# show jalali date in list display 
	list_display = ['name']

	# prepopulated_fields = {'slug': ('name',), }	
	

admin.site.register(Artist)
admin.site.register(Album,FirstModelAdmin)
admin.site.register(Music)