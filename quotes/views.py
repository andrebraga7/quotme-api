from rest_framework import generics
from .models import Quote


class QuoteList(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
