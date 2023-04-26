from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'quote', 'created_at', 'updated_at',
            'content'
        ]


class CommentDetailSerializer(CommentSerializer):

    quote = serializers.ReadOnlyField(source='quote.id')
