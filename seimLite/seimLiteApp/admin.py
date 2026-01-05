from django.contrib import admin
from .models import Project,Log
# Register your models here.

admin.site.register(Project)

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display=("timestamp","level","source","status")
    list_filter=("level","status","source")
    search_fields=("message",)