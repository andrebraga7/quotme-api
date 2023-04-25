from rest_framework import generics, permissions
from .models import Quote
from .serializers import QuoteSerializer


class QuoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
