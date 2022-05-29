from django.contrib import admin
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe

from .models import User, Skill, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'name']
	list_display_links = ['username']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'company', 'company_email', 'get_avatar', 'phone_number']

	def get_avatar(self, obj):
		return mark_safe(f'<img src="{obj.avatar_url}"  style="width: 30px; border-radius: 70%;"/>')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ['skill']