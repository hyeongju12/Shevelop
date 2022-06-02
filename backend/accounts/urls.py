from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

# router = DefaultRouter()
# router.register('users', views.UserViewset)

urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	path('token/', obtain_jwt_token),
	path('token/refresh/', refresh_jwt_token),
	path('token/verify/', verify_jwt_token),
]