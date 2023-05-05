from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from quotme_api.permissions import IsStaffOrReadOnly
from .models import Author
from .serializers import AuthorSerializer


class AuthorList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.annotate(
        quotes_count=Count('quote', distinct=True)
    )

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'id',
    ]
    search_fields = [
        'name',
        'quotes_count',
    ]
    ordering_fields = [
        'name',
        'quotes_count',
    ]


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.annotate(
        quotes_count=Count('quote', distinct=True)
    )
