from django.contrib import admin
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe

from .models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'name']
	list_display_links = ['username']

	def get_avatar(self, obj):
		return mark_safe(f'<img src="{obj.avatar_url}"  style="width: 30px; border-radius: 70%;"/>')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'company', 'company_email', 'phone_number']
