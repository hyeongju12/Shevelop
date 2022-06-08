from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostListUpdateViewSet

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register(r"posts/(?P<post_pk>\d+)/comments", views.CommentViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api/profile/posts/', PostListUpdateViewSet.as_view({'get': 'list'})),
	path('api/profile/posts/<int:pk>/edit/', PostListUpdateViewSet.as_view({'patch': 'partial_update'})),
	# path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
	# path('public/', views.post_list, name='post_list'),
	# path('public/<int:pk>/', views.post_detail, name='post_detail'),
	# path('public/<int:pk>/delete/', views.post_delete, name='post_delete'),
	# path('public/create/', views.post_create, name='post_create'),
]