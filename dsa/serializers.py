from rest_framework import serializers
from .models import Dsa, Tag, Vote

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", 'evote', 'mvote', 'dvote', 'ivote']

class DsaSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    votes = VoteSerializer(many=True)

    class Meta:
        model = Dsa
        fields = ['id', 'name', 'url', 'tags', 'votes']
