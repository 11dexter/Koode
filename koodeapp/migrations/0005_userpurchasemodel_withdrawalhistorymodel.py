# Generated by Django 5.1.1 on 2024-10-02 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koodeapp', '0004_callpackagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPurchaseModel',
            fields=[
                ('user_purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_date', models.DateTimeField()),
                ('purchase_amount', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koodeapp.customermodel')),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawalHistoryModel',
            fields=[
                ('agent_purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('withdrawal_amount', models.FloatField()),
                ('withdrawal_date', models.DateTimeField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koodeapp.customermodel')),
            ],
        ),
    ]
