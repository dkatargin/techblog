from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Entity, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


class EntityAdmin(SummernoteModelAdmin):
    list_display = ("id", "slug", "title", "creation_date", "edit_date")
    summernote_fields = ("text",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Entity, EntityAdmin)
