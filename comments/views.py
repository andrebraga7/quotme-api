from django.db.models import Count
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from quotme_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate(
        replies_count=Count('reply', distinct=True)
    )
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'quote',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        replies_count=Count('reply', distinct=True)
    )
