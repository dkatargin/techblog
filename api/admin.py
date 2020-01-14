from django.contrib import admin
from .models import Entity


class EntityAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'title', 'creation_date', 'edit_date')


admin.site.register(Entity, EntityAdmin)
