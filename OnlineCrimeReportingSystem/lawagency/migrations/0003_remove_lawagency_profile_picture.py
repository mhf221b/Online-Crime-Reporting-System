# Generated by Django 3.1.7 on 2021-04-08 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lawagency', '0002_lawagency_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawagency',
            name='profile_picture',
        ),
    ]
