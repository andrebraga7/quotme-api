from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Reply


class ReplySerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        user = self.context['request'].user
        return user == obj.owner

    def get_created_at(sel, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(sel, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Reply
        fields = [
            'id', 'owner', 'comment', 'created_at', 'updated_at',
            'content', 'is_owner', 'profile_id', 'profile_image'
        ]


class ReplyDetailSerializer(ReplySerializer):

    comment = serializers.ReadOnlyField(source='comment.id')
