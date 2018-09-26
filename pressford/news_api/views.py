from django.shortcuts import render

from rest_framework import generics
from .serializers import NewslistSerializer, CommentsSerializer
from .models import News, Comments

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = News.objects.all()
    serializer_class = NewslistSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def perform_create(self, serializer):
        """Save the post data when creating a new newslist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = News.objects.all()
    serializer_class = NewslistSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CommentList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            news_id=self.kwargs['pk'])

class CommentReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'comments_id'

    def get_queryset(self):
        comment = self.kwargs['comments_id']
        return Comments.objects.filter(id=comment)
