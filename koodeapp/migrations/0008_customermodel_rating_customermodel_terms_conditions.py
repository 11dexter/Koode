# Generated by Django 5.1.1 on 2024-10-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koodeapp', '0007_paymentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customermodel',
            name='terms_conditions',
            field=models.BooleanField(default=False),
        ),
    ]
