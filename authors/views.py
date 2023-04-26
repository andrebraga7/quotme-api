from rest_framework import generics, permissions
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


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AuthorSerializer
    queryset = Author.objects.annotate(
        quotes_count=Count('quote', distinct=True)
    )
