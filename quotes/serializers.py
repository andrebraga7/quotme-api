from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    author = serializers.CharField()

    class Meta:
        model = Quote
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'category',
            'author', 'content'
        ]
