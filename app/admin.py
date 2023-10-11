from django.contrib import admin

from app.models import Log


# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ["ipaddress", "result", "created_at"]
