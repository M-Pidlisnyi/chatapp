# Generated by Django 4.0 on 2022-02-04 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_message_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
    ]
