from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        user = self.context['request'].user
        return user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at', 'name',
            'bio', 'image'
        ]