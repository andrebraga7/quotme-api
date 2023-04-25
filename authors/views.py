from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer


class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
