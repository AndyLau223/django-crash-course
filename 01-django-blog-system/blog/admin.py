from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author', 'slug')


# Register your models here.
admin.site.register(Post, PostAdmin)
