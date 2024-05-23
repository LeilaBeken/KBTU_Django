# Generated by Django 5.0.6 on 2024-05-22 12:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_userbankaccount_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccounttype',
            name='annual_interest_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Interest rate from 0 - 100', max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccounttype',
            name='interest_calculation_per_year',
            field=models.PositiveSmallIntegerField(default=1, help_text='The number of times interest will be calculated per year', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankaccounttype',
            name='maximum_withdrawal_amount',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=12),
            preserve_default=False,
        ),
    ]
