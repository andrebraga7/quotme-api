from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):

    quotes_count = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = [
            'id', 'name', 'quotes_count'
        ]
