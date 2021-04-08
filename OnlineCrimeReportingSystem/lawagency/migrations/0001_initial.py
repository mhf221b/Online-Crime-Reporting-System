# Generated by Django 3.1.7 on 2021-04-06 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LawAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_ID', models.CharField(db_column='Agency ID', max_length=10, unique=True)),
                ('agency_branch', models.CharField(db_column='Agency Branch', max_length=10)),
                ('usertype', models.CharField(db_column='User Type', default='Law Agency', max_length=15)),
                ('user', models.OneToOneField(db_column='User ID', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
