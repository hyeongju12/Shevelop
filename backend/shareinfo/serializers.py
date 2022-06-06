import re
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, Comment


class AuthorSerializer(ModelSerializer):
	avatar_url = serializers.SerializerMethodField("avatar_url_field")

	def avatar_url_field(self, author):
		if re.match(r"^https?://", author.avatar_url):
			return author.avatar_url
		if 'request' in self.context:
			scheme = self.context['request'].scheme
			host = self.context['request'].get_host()
			return scheme + '://' + host + author.avatar_url

		request

	class Meta:
		model = get_user_model()
		fields = ['username', "name", "avatar_url"]


class PostSerializer(ModelSerializer):
	author = AuthorSerializer(read_only=True)
	is_like = serializers.SerializerMethodField("post_likes_field")
	post_tag_set = serializers.CharField(source='extract_tag_list', read_only=True)

	class Meta:
		model = Post
		fields = ['author', 'is_like', 'post_tag_set', 'title'
			, 'category', 'content', 'attached_file', 'cover_img'
			, 'is_public', 'created_at', 'updated_at', 'id']

	def post_likes_field(self, post):
		if 'request' in self.context:
			user = self.context['request'].user
			return post.like_user_set.filter(pk=user.pk).exists()
		return False


class CommentSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True)

	class Meta:
		model = Comment
		fields = ["id", "author", "message", 'created_at']
