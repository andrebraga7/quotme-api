from django.db.models import Count
from rest_framework import generics, permissions
from .models import Quote
from authors.models import Author
from .serializers import QuoteSerializer
from quotme_api.permissions import IsOwnerOrReadOnly


class QuoteList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.annotate(
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')

    def perform_create(self, serializer):
        # Retrieve the author name from the serializer validated_data
        # Get or create a new author instance with the given name
        # Save method to create a new quote instance
        name = serializer.validated_data['author']
        author_instance, created = Author.objects.get_or_create(name=name)
        serializer.save(owner=self.request.user, author=author_instance)


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.annotate(
        likes_count=Count('likes', distinct=True)
    )

    def perform_update(self, serializer):
        # Same logic as the perform_create but this will run when updating
        name = serializer.validated_data['author']
        author_instance, created = Author.objects.get_or_create(name=name)
        serializer.save(author=author_instance)
