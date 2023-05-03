from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Quote
from authors.models import Author
from .serializers import QuoteSerializer
from quotme_api.permissions import IsOwnerOrReadOnly


class QuoteList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'category',
        'author',
    ]
    search_fields = [
        'owner__username',
        'category',
        'author__name',
        'content',
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at'
    ]

    def perform_create(self, serializer):
        name = serializer.validated_data['author']
        author_instance, created = Author.objects.get_or_create(name=name)
        serializer.save(owner=self.request.user, author=author_instance)


class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')

    def perform_update(self, serializer):
        name = serializer.validated_data['author']
        author_instance, created = Author.objects.get_or_create(name=name)
        serializer.save(author=author_instance)
