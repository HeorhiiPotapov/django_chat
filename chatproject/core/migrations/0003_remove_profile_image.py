# Generated by Django 3.1 on 2020-08-20 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_room_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]