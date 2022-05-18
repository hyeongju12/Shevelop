from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


class PostListCreateAPIView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
