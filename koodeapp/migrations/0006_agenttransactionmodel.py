# Generated by Django 5.1.1 on 2024-10-04 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koodeapp', '0005_userpurchasemodel_withdrawalhistorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentTransactionModel',
            fields=[
                ('agent_transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_amount', models.FloatField()),
                ('transaction_date', models.DateTimeField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='koodeapp.customermodel')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_transactions', to='koodeapp.customermodel')),
            ],
        ),
    ]
