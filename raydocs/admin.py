from django.contrib import admin
from .models import MyIdea
# Register your models here.
@admin.register(MyIdea)
class AdminIdea(admin.ModelAdmin):
    list_display = ['id','name','idea']