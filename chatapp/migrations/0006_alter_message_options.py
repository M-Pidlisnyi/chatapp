# Generated by Django 4.0 on 2022-02-04 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-time']},
        ),
    ]