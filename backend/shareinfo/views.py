from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import get_object_or_404
from .serializers import PostSerializer, CommentSerializer, PostListSerializer
from .models import Post, Comment


class PostListUpdateViewSet(ViewSet):
	def list(self, request):
		queryset = Post.objects.all().filter(author=self.request.user)
		serializer = PostListSerializer(queryset, many=True)
		return Response(serializer.data)

	def partial_update(self, request, pk=None):
		post = Post.objects.filter(author=self.request.user).get(pk=pk)
		serializer = PostListSerializer(instance=post, data=request.data, partial=True)
		if serializer.is_valid():
			if serializer.data['author'] != self.request.user:
				return Response(status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
			serializer.save()
			return Response(serializer.data, status.HTTP_200_OK)
		return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all().filter(is_public=True)
	parser_classes = [MultiPartParser, FormParser]
	serializer_class = PostSerializer

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["request"] = self.request
		return context

	def get_queryset(self):
		qs = super().get_queryset()
		qs = qs.filter(
			Q(author=self.request.user) |
			Q(author__in=self.request.user.following_set.all())
		)
		return qs

	def perform_create(self, serializer):
		serializer.save(author=self.request.user, ip=self.request.META['REMOTE_ADDR'])
		return super().perform_create(serializer)

	@action(detail=True, methods=["POST"])
	def like(self, request, pk):
		post = self.get_object()
		post.like_user_set.add(self.request.user)
		return Response(status.HTTP_201_CREATED)

	@like.mapping.delete
	def unlike(self, request, pk):
		post = self.get_object()
		post.like_user_set.remove(self.request.user)
		return Response(status.HTTP_204_NO_CONTENT)


class CommentViewSet(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["request"] = self.request
		return context

	def get_queryset(self):
		qs = super().get_queryset()
		qs = qs.filter(post__pk=self.kwargs['post_pk'])
		return qs

	def perform_create(self, serializer):
		post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
		serializer.save(author=self.request.user, comment_ip=self.request.META['REMOTE_ADDR'], post=post)
		return super().perform_create(serializer)