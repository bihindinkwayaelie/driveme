from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Driver)
# admin.site.register(Client)

admin.site.site_header = 'DriveMe administration'

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','phonenumber','approved')
    ordering = ('fullname',)
    search_fields = ('fullname','email')
    list_filter = ('created','workingtime','approved','working')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fullname','email','phonenumber','served')
    ordering = ('fullname',)
    search_fields = ('fullname','email')
    list_filter = ('created','served')