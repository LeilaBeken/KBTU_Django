# Generated by Django 5.0.1 on 2024-02-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('email_address', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('roll_number', models.IntegerField()),
            ],
        ),
    ]