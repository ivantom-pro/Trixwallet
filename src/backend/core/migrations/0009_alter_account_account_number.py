# Generated by Django 4.1.3 on 2022-12-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_account_display_currency_alter_account_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.BigIntegerField(default=1000001, editable=False, unique=True),
        ),
    ]
