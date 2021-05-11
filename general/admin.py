from django.contrib import admin
from .models import *  
# Register your models here.






from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from jalali_date import datetime2jalali, date2jalali
	
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
	# show jalali date in list display 
	list_display = ['name', 'get_created_jalali']
	
	
	def get_created_jalali(self, obj):
		return date2jalali(obj.date).strftime('%y/%m/%d ')
	
	get_created_jalali.short_description = 'تاریخ ایجاد'
	get_created_jalali.admin_order_field = 'created'


admin.site.register(Artist)
admin.site.register(Album,FirstModelAdmin)
admin.site.register(Music)