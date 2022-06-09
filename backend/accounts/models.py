from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from annoying.fields import AutoOneToOneField

class User(AbstractUser):
	avatar = models.ImageField(blank=True, upload_to='accounts/avatar/%Y/%m/%d',
								help_text = "48px * 48px 크기의 png/jpg를 넣어주세요. ")
	follower_set = models.ManyToManyField("self", blank=True)
	following_set = models.ManyToManyField("self", blank=True)
	recommended = models.ManyToManyField('self', blank=True)
	is_active = models.BooleanField(default=True)

	@property
	def name(self):
		return f"{self.first_name}{self.last_name}".strip()

	@property
	def avatar_url(self):
		if self.avatar:
			return self.avatar.url
		else:
			return resolve_url('pydenticon_image', self.username)


class Profile(models.Model):
	user = AutoOneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
	website_url = models.URLField(default='')
	company = models.CharField(max_length=20, default='Settings에서 정보를 입력해주세요')
	company_email = models.EmailField(max_length=50, default='Settings에서 정보를 입력해주세요')
	bio = models.TextField(default='Settings에서 정보를 입력해주세요')
	skill_set = models.CharField(max_length=20, default='Settings에서 정보를 입력해주세요')
	location = models.CharField(max_length=100, blank=True)
	phone_number = models.CharField(max_length=14, validators=[RegexValidator(r'^010-?[\d]{4}-?[\d]{4}$')], blank=True)
	available = models.TextField(blank=True)