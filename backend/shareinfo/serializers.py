import re
import os
import dotenv
from shevelop.settings.common import BASE_DIR
import re
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, Comment

dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
	dotenv.load_dotenv(dotenv_file)
HOST = os.environ['HOST']


class AuthorSerializer(ModelSerializer):
	avatar_url = serializers.SerializerMethodField("avatar_url_field", read_only=True)

	def avatar_url_field(self, user):
		return HOST + user.avatar_url

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


class PostListSerializer(ModelSerializer):
	author = AuthorSerializer(read_only=True)
	post_tag_set = serializers.CharField(source='extract_tag_list', read_only=True)

	class Meta:
		model = Post
		fields = ['author', 'post_tag_set', 'title'
			, 'category', 'content', 'attached_file', 'cover_img'
			, 'is_public', 'created_at', 'updated_at', 'id']


class PostUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'category', 'content', 'attached_file', 'cover_img']

		def update(self, instance, validated_data):
			instance.cover_img = validated_data.get('cover_img', instance.cover_img)
			instance.save()
			return instance


class PostImageUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = ['cover_img']


class CommentSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True)

	class Meta:
		model = Comment
		fields = ["id", "author", "message", 'created_at']
