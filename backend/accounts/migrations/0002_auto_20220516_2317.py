# Generated by Django 3.2 on 2022-05-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='skill_set',
        ),
        migrations.AddField(
            model_name='user',
            name='skill_set',
            field=models.ManyToManyField(blank=True, to='accounts.Skill'),
        ),
    ]
