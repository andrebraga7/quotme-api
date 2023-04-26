from rest_framework import generics, permissions
from quotme_api.permissions import IsOwnerOrReadOnly
from .models import Reply
from .serializers import ReplySerializer, ReplyDetailSerializer


class ReplyList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
