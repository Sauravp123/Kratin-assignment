from django.contrib import admin
from .models import Category, Patient


class CategoryAdmin(admin.ModelAdmin):
	list_display=['name']
	#prepopulated_fields={'slug': ('name',)}



class PatientAdmin(admin.ModelAdmin):
	list_display=['name','category','address','available','created','updated']
	list_filter=['available','created','updated','category']
	list_editable=['available']
	#prepopulated_fields={'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Patient, PatientAdmin)
