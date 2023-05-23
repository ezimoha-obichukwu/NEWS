from django.contrib import admin
from .models import News

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "reporter"]
    prepopulated_fields = {'slug': ('title',)}

