# Generated by Django 4.1.3 on 2023-01-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_account_account_number_alter_deposit_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='1000000', max_length=40, unique=True),
        ),
    ]
