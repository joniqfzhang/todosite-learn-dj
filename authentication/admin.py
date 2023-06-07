from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# customise UserAdmin
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email', 'is_staff')
    #  specify pagination
    list_per_page = 10

admin.site.register(User, UserAdmin)