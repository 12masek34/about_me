from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',)
    list_display_links = ('title',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Image)
