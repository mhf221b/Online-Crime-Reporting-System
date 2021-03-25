# Generated by Django 3.1.7 on 2021-03-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nid', models.IntegerField()),
                ('email', models.TextField()),
                ('home_address', models.TextField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
            options={
                'unique_together': {('nid', 'email', 'mobile_number')},
            },
        ),
    ]
