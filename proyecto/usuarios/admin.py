from django.contrib import admin

from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'tipo_usuario')

admin.site.register(User, UserAdmin)
