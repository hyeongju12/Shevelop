from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets

from .models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['company', 'bio', 'skill_set']


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

	class Meta:
		model = User
		fields = ["profile", "username", "name", "avatar_url"]