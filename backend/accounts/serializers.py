import re
import os
import dotenv
from shevelop.settings.common import BASE_DIR
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile

dotenv_file = os.path.join(BASE_DIR, '.env')
if os.path.isfile(dotenv_file):
	dotenv.load_dotenv(dotenv_file)
HOST = os.environ['HOST']

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['bio', 'skill_set', 'company',  'company_email']


class UserSerializer(serializers.ModelSerializer):
	avatar_url = serializers.SerializerMethodField("avatar_url_field", read_only=True)

	def avatar_url_field(self, user):
		return HOST + user.avatar_url

	class Meta:
		model = User
		fields = ['id', 'avatar', 'avatar_url', 'email', 'first_name', 'last_name', 'is_active']


class SignupSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	def create(self, validated_data):
		user = User.objects.create(username=validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ['pk', 'username', 'email', 'password']


class SuggestionUserSerializer(serializers.ModelSerializer):
	profile = ProfileSerializer()
	avatar_url = serializers.SerializerMethodField("avatar_url_field")

	def avatar_url_field(self, user):
		if re.match(r"^https?://", user.avatar_url):
			return User.avatar_url
		if 'request' in self.context:
			scheme = self.context['request'].scheme
			host = self.context['request'].get_host()
			return scheme + '://' + host + user.avatar_url

		request

	class Meta:
		model = User
		fields = ["profile", "username", "name", "avatar_url"]
