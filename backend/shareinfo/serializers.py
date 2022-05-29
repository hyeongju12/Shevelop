from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post


class AuthorSerializer(ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ['username']


class PostSerializer(ModelSerializer):
	author = AuthorSerializer(read_only=True)
	is_like = serializers.SerializerMethodField("post_likes_field")

	def post_likes_field(self, post):
		if 'request' in self.context:
			user = self.context['request'].user
			return post.post_likes.filter(pk=user.pk).exists()
		return False

	class Meta:
		model = Post
		fields = '__all__'
