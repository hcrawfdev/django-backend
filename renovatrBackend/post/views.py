from django.shortcuts import render

from post.models import Post
from post.permissions import IsOwnerOrReadOnly

from post.serializers import (
    ListSerializer,
    DetailSerializer,
    PostCreateSerializer,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostCreateView(CreateAPIView):
	serializer_class=PostCreateSerializer
	def perform_create(self,serializer):
		serializer.save(author=self.request.user)
		
class PostDeleteView(DestroyAPIView):
	queryset=Post.objects.all()
	serializer_class=ListSerializer
	lookup_field='pk'

class PostListView(ListAPIView):
	queryset=Post.objects.all()
	serializer_class=ListSerializer

class PostDetailView(RetrieveAPIView):
	queryset=Post.objects.all()
	serializer_class=ListSerializer
	lookup_field='pk'

class PostUpdateView(RetrieveUpdateAPIView):
	queryset=Post.objects.all()
	serializer_class=PostCreateSerializer
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field='pk'