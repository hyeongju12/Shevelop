# Generated by Django 3.2 on 2022-06-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareinfo', '0009_auto_20220604_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
