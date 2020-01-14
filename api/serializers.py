from rest_framework import serializers
from .models import Entity

preview_length = 140


class EntitySerializer(serializers.ModelSerializer):
    preview = serializers.SerializerMethodField()

    def get_preview(self, obj):
        result = obj.text[:preview_length]
        if len(obj.text) > preview_length:
            result += '...'
        return result

    class Meta:
        model = Entity
        fields = ('slug', 'title', 'preview', 'creation_date', 'edit_date')


class EntityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'
