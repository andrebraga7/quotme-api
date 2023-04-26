from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    author = serializers.CharField()
    likes_count = serializers.ReadOnlyField()

    class Meta:
        model = Quote
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'category',
            'author', 'content', 'likes_count'
        ]
