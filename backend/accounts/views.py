from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404
from rest_framework.views import APIView
from .serializers import SignupSerializer, SuggestionUserSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

User = get_user_model()


class SignupView(CreateAPIView):
	model = User
	serializer_class = SignupSerializer
	permission_classes = [AllowAny]


class UserInfoView(APIView):
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]
	http_method_names = ['GET']

	def get_object(self, username):
		user = get_object_or_404(User, username=username)
		return user

	def get(self, request, format=None):
		userinfo = self.get_object(username=request.user.username)
		serializer = UserSerializer(userinfo)
		return Response(serializer.data)


class SuggestionListAPIView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = SuggestionUserSerializer

	def get_queryset(self):
		qs = super().get_queryset()
		qs = qs.exclude(username=self.request.user.username)
		qs = qs.exclude(pk__in=self.request.user.following_set.all())
		return qs

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["request"] = self.request
		return context


class FollowingUserListAPIView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = SuggestionUserSerializer

	def get_queryset(self):
		qs = super().get_queryset()
		qs = qs.exclude(username=self.request.user.username)
		qs = qs.filter(pk__in=self.request.user.following_set.all())
		return qs

	def get_serializer_context(self):
		context = super().get_serializer_context()
		context["request"] = self.request
		return context


@api_view(["POST"])
def user_follow(request):
	username = request.data['username']
	follow_user = get_object_or_404(User, username=username, is_active=True)
	request.user.following_set.add(follow_user)
	follow_user.follower_set.add(request.user)
	return Response(status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def user_unfollow(request):
	username = request.data['username']
	follow_user = get_object_or_404(User, username=username, is_active=True)
	request.user.following_set.remove(follow_user)
	follow_user.follower_set.remove(request.user)
	return Response("삭제되었습니다.")