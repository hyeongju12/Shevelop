from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostListUpdateViewSet

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register(r"posts/(?P<post_pk>\d+)/comments", views.CommentViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api/set/', PostListUpdateViewSet.as_view({'get': 'list'})),
	path('api/set/<int:pk>/edit/', PostListUpdateViewSet.as_view({'patch': 'partial_update'})),
	path('api/set/<int:pk>/delete/', PostListUpdateViewSet.as_view({'delete': 'destroy'})),
]