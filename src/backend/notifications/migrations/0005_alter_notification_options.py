# Generated by Django 4.1.3 on 2022-12-05 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_notification_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
