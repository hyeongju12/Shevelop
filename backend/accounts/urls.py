from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from . import views

from .views import UserUpdateView, ProfileUpdateView

urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('withdrawal/', views.WithdrawalView.as_view(), name='withdrawal'),
	path('change/', views.ChangePasswordView.as_view(), name='change_password'),
	path('token/', obtain_jwt_token),
	path('token/refresh/', refresh_jwt_token),
	path('token/verify/', verify_jwt_token),
	path('profile/', ProfileUpdateView.as_view(), name="profile_edit"),
	path('user/', UserUpdateView.as_view(), name="user_edit"),
	path('suggestions/', views.SuggestionListAPIView.as_view(), name="suggestion_user_list"),
	path('followings/', views.FollowingUserListAPIView.as_view(), name="following_user_list"),
	path('follow/', views.user_follow, name='user_follow'),
	path('unfollow/', views.user_unfollow, name='user_unfollow'),
]