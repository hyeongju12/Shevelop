from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'content', 'cover_img']
	search_fields = ['content']

	def cover_img(self, obj):
		return mark_safe(f'<img src={obj.cover_img_url} style="width: 50px; height: 50px; "/>')