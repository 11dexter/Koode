# Generated by Django 5.1.1 on 2024-10-07 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koodeapp', '0006_agenttransactionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('razorpay_id', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_signature', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koodeapp.customermodel')),
            ],
        ),
    ]