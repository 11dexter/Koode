# Generated by Django 5.1.1 on 2024-10-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koodeapp', '0014_alter_customermodel_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='customer_phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
