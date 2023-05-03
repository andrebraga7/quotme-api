from rest_framework import serializers
from .models import Quote
from likes.models import Like
from saved.models import Save


class QuoteSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    author = serializers.CharField()
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    save_id = serializers.SerializerMethodField()
    author_id = serializers.ReadOnlyField(source='author.id')
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        user = self.context['request'].user
        return user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, quote=obj
            ).first()
            return like.id if like else None
        return None

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, quote=obj
            ).first()
            return save.id if save else None
        return None

    class Meta:
        model = Quote
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'category',
            'author', 'content', 'is_owner', 'profile_id', 'profile_image',
            'like_id', 'save_id', 'author_id', 'comments_count', 'likes_count'
        ]
