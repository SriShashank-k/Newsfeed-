from django.contrib import admin
from .models import Headline

@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'source_name', 'published_at', 'category', 'country', 'language')
    search_fields = ('title', 'description', 'source_name', 'category', 'country', 'language')
    list_filter = ('source_name', 'published_at', 'category', 'country', 'language')
    fields = ('title', 'description', 'url', 'source_name', 'published_at', 'category', 'country', 'language')