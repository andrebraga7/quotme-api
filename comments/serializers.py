from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    replies_count = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'quote', 'created_at', 'updated_at',
            'content', 'replies_count'
        ]


class CommentDetailSerializer(CommentSerializer):

    quote = serializers.ReadOnlyField(source='quote.id')
