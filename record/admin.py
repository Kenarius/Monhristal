from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'record_type', 'day')
    list_filter = ('name', 'record_type', 'day')
    search_fields = ('name', 'day')
    ordering = ('day', 'name')
