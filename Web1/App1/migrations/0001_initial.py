# Generated by Django 5.0.2 on 2024-03-01 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Emails', models.CharField(max_length=30)),
                ('Contact_no', models.IntegerField(verbose_name=12)),
                ('Address', models.TextField()),
            ],
        ),
    ]