# Generated by Django 5.1.1 on 2024-09-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminmodel',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_first_name', models.CharField(max_length=255)),
                ('admin_last_name', models.CharField(blank=True, max_length=255)),
                ('admin_email', models.EmailField(max_length=254)),
                ('admin_password', models.CharField(max_length=255)),
            ],
        ),
    ]
