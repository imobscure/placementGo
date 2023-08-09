from rest_framework import serializers
from .models import Dsa, Tag, Mark

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']

class DsaSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Dsa
        fields = ['id', 'name', 'url', 'evote', 'mvote', 'dvote', 'ivote', 'tags']

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'username', 'pid', 'date']
