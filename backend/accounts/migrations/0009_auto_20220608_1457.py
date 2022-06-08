# Generated by Django 3.2 on 2022-06-08 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='skill_set',
        ),
        migrations.AddField(
            model_name='profile',
            name='skill_set',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
