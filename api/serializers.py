from rest_framework import serializers
from .models import Entity, Tag

preview_length = 500


class EntityTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class EntitySerializer(serializers.ModelSerializer):
    tags = EntityTagsSerializer(many=True)
    preview = serializers.SerializerMethodField()

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
    class Meta:
        model = Entity
        fields = '__all__'
