# Generated by Django 3.1.7 on 2021-04-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawagency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawagency',
            name='profile_picture',
            field=models.ImageField(db_column='Profile Picture', default='default.jpg', upload_to='profile_pictures'),
        ),
    ]
