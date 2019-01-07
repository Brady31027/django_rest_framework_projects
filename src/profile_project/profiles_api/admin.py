from django.contrib import admin
from . import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_login', 'is_staff', 'is_superuser')

# Register your models here.
admin.site.register(models.UserProfile, UserProfileAdmin)