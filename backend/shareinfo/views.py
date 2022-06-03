from datetime import timedelta
from django.db.models import Q
from django.http import Http404
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from rest_framework import generics, status
# from .permissions import IsAuthorOrReadonly
from django.utils import timezone
from .serializers import PostSerializer
from .models import Post


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get_queryset(self):
		timesince = timezone.now() - timedelta(days=3)
		qs = super().get_queryset()
		qs = qs.filter(
			Q(author=self.request.user) |
			Q(author__in=self.request.user.following_set.all())
		)
		qs = qs.filter(created_at__gte = timesince)
		return qs
	# permission_classes = [AllowAny]



#APIView 상속받아 ListView 기능 구현
# class PostListAPIView(APIView):
# 	def get(self, request):
# 		qs = Post.objects.all()
# 		serializer = PostSerializer(qs, many=True)
# 		return Response(serializer.data)
#
#
# post_list = PostListAPIView.as_view()


#APIView > DetailAPIView
# class PostDetailAPIView(APIView):
#
# 		def get(self, request, pk):
# 			qs = Post.objects.get(pk=pk)
# 			if qs:
# 				serializer = PostSerializer(qs)
# 				return Response(serializer.data)
# 			else:
# 				return Http404
# post_detail = PostDetailAPIView.as_view()

# @api_view(['GET'])
# def post_detail(request, pk):
# 	if request.method == 'GET':
# 		qs = Post.objects.get(pk=pk)
# 		serializer = PostSerializer(qs)
# 		return Response(serializer.data)
# 	return Response(status=status.HTTP_404_NOT_FOUND)
# class PostDetailAPIView(RetrieveAPIView):
# 	queryset = Post.objects.all()
# 	renderer_classes = [TemplateHTMLRenderer]
# 	template_name = 'shareinfo/post_detail.html'
#
# 	def get(self, request, *args, **kwargs):
# 		post = self.get_object()
# 		serializer = PostSerializer(post)
# 		return Response({
# 			# 'post' : serializer.data,
# 			'post' : post,
# 		})

#------------------------------------------------------------------------------------------------


# class PostDeleteAPIView(APIView):
# 	def delete(self, request, pk):
# 		qs = Post.objects.get(pk=pk)
# 		if qs:
# 			qs.delete()
# 			return Response(status=status.HTTP_204_NO_CONTENT)
# 		else:
# 			return Http404


# @api_view(['DELETE'])
# def post_delete(request, pk):
# 	if request.method == 'DELETE':
# 		qs = get_object_or_404(Post, pk=pk)
# 		qs.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
# 	return Response(status=status.HTTP_400_BAD_REQUEST)


# post_delete = PostDeleteAPIView.as_view()

# class PostCreateAPIView(APIView):
# 	def post(self, request, format=None):
# 		serializer = PostSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(status=status.HTTP_400_BAD_REQUEST)
#
# post_create = PostCreateAPIView.as_view()

# @api_view(['GET', 'POST'])
# def post_create(request):
# 	if request.method == 'POST':
# 		serializer = PostSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(status=status.HTTP_400_BAD_REQUEST)
# 	elif request.method == 'GET':
# 		serializer = PostSerializer(Post.objects.all(), many=True)
# 		return Response(serializer.data)


# class PostListCreateAPIView(generics.ListCreateAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer
#
#
# class PostViewSet(ModelViewSet):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer
# 	permission_classes = [IsAuthenticated]
#
# 	filter_backends = [SearchFilter]
# 	search_fields = ['content']
# 	ordering = ['id']
#
# 	@action(detail=False, methods=['GET'])
# 	def public(self, request):
# 		qs = self.get_queryset()
# 		serializer = self.get_serializer(qs, many=True)
# 		# serializer class에서 해당 Serializer을 찾아서 연결해준다.
# 		# serializer = PostSerializer(qs, many=True)
# 		return Response(serializer.data)
#
# 	@action(detail=True, methods=['PATCH'])
# 	def set_public(self, request, pk):
# 		instance = self.get_object()
# 		instance.title = request.data['title']
# 		instance.save()
# 		serializer = PostSerializer(instance)
# 		return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
#
# 	def perform_create(self, serializer):
# 		author = self.request.user
# 		ip = self.request.META['REMOTE_ADDR']
# 		serializer.save(author=author, ip=ip)