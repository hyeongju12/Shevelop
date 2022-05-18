from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
	category = models.CharField(max_length=100, default='all')
	title = models.CharField(max_length=100)
	content = models.TextField()
	attached_file = models.FileField(blank=True)
	cover_img = models.ImageField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	post_tag_set = models.ManyToManyField('Tag', blank=True)
	post_likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def cover_img_url(self):
		if self.cover_img:
			return self.cover_img.url
		else:
			return self.title


class Tag(models.Model):
	tag = models.CharField(max_length=20)
