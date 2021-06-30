from django.contrib import admin
from .models import MyIdea,TotalVisit
# Register your models here.
@admin.register(MyIdea)
class AdminIdea(admin.ModelAdmin):
    list_display = ['id','name','idea']
    
    
@admin.register(TotalVisit)
class AdminVisit(admin.ModelAdmin):
    list_display = ['id','count']