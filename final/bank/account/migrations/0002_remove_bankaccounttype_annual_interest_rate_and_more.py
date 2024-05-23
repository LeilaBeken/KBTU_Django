# Generated by Django 5.0.6 on 2024-05-22 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccounttype',
            name='annual_interest_rate',
        ),
        migrations.RemoveField(
            model_name='bankaccounttype',
            name='interest_calculation_per_year',
        ),
        migrations.RemoveField(
            model_name='bankaccounttype',
            name='maximum_withdrawal_amount',
        ),
        migrations.AlterField(
            model_name='bankaccounttype',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_type',
            field=models.ForeignKey(limit_choices_to={'name__in': ['Saving Account', 'Checking Account', 'Money Market Account', 'Certificate of Deposit (CD)']}, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='account.bankaccounttype'),
        ),
    ]
