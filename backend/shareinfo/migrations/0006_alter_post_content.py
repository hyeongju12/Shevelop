# Generated by Django 3.2 on 2022-05-31 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareinfo', '0005_rename_tag_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=2000),
        ),
    ]
