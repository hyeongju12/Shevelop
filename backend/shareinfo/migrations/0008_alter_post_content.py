# Generated by Django 3.2 on 2022-05-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareinfo', '0007_rename_post_likes_post_like_user_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]