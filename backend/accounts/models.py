from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url


class User(AbstractUser):
	follower_set = models.ManyToManyField("self", blank=True)
	following_set = models.ManyToManyField("self", blank=True)
	recommended = models.ManyToManyField('self', blank=True)

	@property
	def name(self):
		return f"{self.first_name} {self.last_name}".strip()


class Profile(models.Model):
	user = models.OneToOneField('User', on_delete=models.CASCADE)
	website_url = models.URLField(blank=True)
	company = models.CharField(max_length=20, blank=True)
	company_email = models.EmailField(max_length=50, blank=True)
	bio = models.TextField(blank=True)
	skill_set = models.ManyToManyField('Skill', blank=True)
	location = models.CharField(max_length=100, blank=True)
	phone_number = models.CharField(max_length=14, validators=[RegexValidator(r'^010-?[\d]{4}-?[\d]{4}$')], blank=True)
	avatar = models.ImageField(blank=True, upload_to='accounts/avatar/%Y/%m/%d',
								help_text = "48px * 48px 크기의 png/jpg를 넣어주세요. ")
	available = models.TextField(blank=True)

	@property
	def avatar_url(self):
		if self.avatar:
			return self.avatar.url
		else:
			return resolve_url('pydenticon_image', self.user.username)


class Skill(models.Model):
	skill = models.CharField(max_length=20)

	def __str__(self):
		return self.skill