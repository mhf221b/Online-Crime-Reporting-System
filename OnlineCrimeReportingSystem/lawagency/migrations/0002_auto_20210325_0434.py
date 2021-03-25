# Generated by Django 3.1.7 on 2021-03-24 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawagency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawagency',
            name='agency_branch',
            field=models.CharField(db_column='Agency Branch', max_length=10),
        ),
        migrations.AlterField(
            model_name='lawagency',
            name='email',
            field=models.TextField(db_column='Email Address'),
        ),
        migrations.AlterField(
            model_name='lawagency',
            name='name',
            field=models.TextField(db_column='Name'),
        ),
        migrations.AlterField(
            model_name='lawagency',
            name='password',
            field=models.CharField(db_column='Password', max_length=15),
        ),
        migrations.AlterField(
            model_name='lawagency',
            name='user_id',
            field=models.IntegerField(db_column='User ID'),
        ),
    ]
