# Generated by Django 3.1.7 on 2021-04-01 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crimereports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(db_column='Complaint Status', max_length=10)),
                ('complaint_history', models.CharField(db_column='Complaint History', max_length=10)),
                ('date', models.CharField(db_column='Date', max_length=10)),
                ('crime_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crimereports.crimereports')),
            ],
        ),
    ]
