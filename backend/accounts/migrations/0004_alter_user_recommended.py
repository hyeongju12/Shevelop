# Generated by Django 3.2 on 2022-05-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220518_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recommended',
            field=models.IntegerField(default=0),
        ),
    ]
