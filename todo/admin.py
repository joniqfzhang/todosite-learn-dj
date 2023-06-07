from django.contrib import admin
from .models import Todo


# Register your models here.
# Register Todo models so admin can display Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed')
    search_fields = ('title', 'description', 'is_completed')
    #  specify pagination
    list_per_page = 25


admin.site.register(Todo, TodoAdmin)
