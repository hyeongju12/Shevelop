import re
from rest_framework.reverse import reverse
from django.conf import settings
from django.db import models


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Post(BaseModel):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
	category = models.CharField(max_length=100, default='all')
	title = models.CharField(max_length=100)
	content = models.TextField()
	attached_file = models.FileField(blank=True, upload_to="shareinfo/post/cover/%Y/%m/%d")
	cover_img = models.ImageField(blank=True, upload_to="shareinfo/post/cover/%Y/%m/%d")
	post_tag_set = models.ManyToManyField('Tag', blank=True)
	like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
	ip = models.GenericIPAddressField(null=True, editable=False)

	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def cover_img_url(self):
		if self.cover_img:
			return self.cover_img.url
		else:
			return self.title

	def get_absolute_url(self):
		return reverse('shareinfo:post_detail', args=[self.pk])

	def extract_tag_list(self):
		tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.content)
		tag_list = []
		for tag_name in tag_name_list:
			tag, _  = Tag.objects.get_or_create(name=tag_name) # tag 반환값, 반환결과에 대한 불리언 값
			tag_list.append(tag)
		return tag_list

	def is_like_user(self, user):
		return self.like_user_set.filter(pk=user.pk).exists()


class Comment(BaseModel):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	message = models.TextField()

	class Meta:
		ordering = ["-id"]


class Tag(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name
