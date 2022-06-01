from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

# router = DefaultRouter()
# router.register('users', views.UserViewset)

urlpatterns = [
	path('signup/', views.SignupView.as_view(), name='signup'),
	# path('', include(router.urls)),
	# path('api-token-auth/', obtain_auth_token),
	# path('api-jwt-auth/', obtain_jwt_token),
	# path('api-jwt-auth/refresh/', refresh_jwt_token),
	# path('api-jwt-auth/verify/', verify_jwt_token),
]