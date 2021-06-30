from django.contrib import admin
from .models import MyIdea
# Register your models here.
class AdminIdea(admin.ModelAdmin):
    list_display = ['id','name','idea']