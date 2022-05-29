from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	# path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
	# path('public/', views.post_list, name='post_list'),
	# path('public/<int:pk>/', views.post_detail, name='post_detail'),
	# path('public/<int:pk>/delete/', views.post_delete, name='post_delete'),
	# path('public/create/', views.post_create, name='post_create'),
]