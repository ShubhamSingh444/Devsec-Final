from django.contrib import admin
from .models import UserProfileç
# Register your models here.
from .models import Addmoney_info

class Addmoney_infoAdmin(admin.ModelAdmin):
    list_display=("user","quantity","Date","Category","add_money")
admin.site.register(Addmoney_info,Addmoney_infoAdmin)
from django.contrib.sessions.models import Session
admin.site.register(Session)

admin.site.register(UserProfile)
