"""
Admin configuration for models in the Django app.
"""
from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import UserProfile
# Register your models here.
from .models import Addmoney_info

class Addmoney_infoAdmin(admin.ModelAdmin):
    """
    Admin model configuration for the 'Addmoney_info' model.
    """
    list_display=("user","quantity","Date","Category","add_money")
admin.site.register(Addmoney_info,Addmoney_infoAdmin)

admin.site.register(Session)

admin.site.register(UserProfile)
