# Generated by Django 3.2 on 2022-05-28 07:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_recommended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='recommended',
        ),
        migrations.AddField(
            model_name='user',
            name='recommended',
            field=models.ManyToManyField(blank=True, related_name='_accounts_user_recommended_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
