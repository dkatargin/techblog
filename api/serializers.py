from rest_framework import serializers
from .models import Entity, Tag

preview_length = 500


class EntityTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class EntitySerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    preview = serializers.SerializerMethodField()

    @staticmethod
    def get_tags(instance):
        return [t.name for t in instance.tags.all()]

    @staticmethod
    def get_preview(obj):
        result = obj.text[:preview_length]
        if len(obj.text) > preview_length:
            result += '...'
        return result

    class Meta:
        model = Entity
        fields = ('slug', 'title', 'preview', 'creation_date', 'edit_date', 'tags')


class EntityDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    @staticmethod
    def get_tags(instance):
        return [t.name for t in instance.tags.all()]

    class Meta:
        model = Entity
        fields = '__all__'
