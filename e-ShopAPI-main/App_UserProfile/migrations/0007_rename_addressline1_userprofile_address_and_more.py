# Generated by Django 4.0.5 on 2022-09-12 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_UserProfile', '0006_alter_userprofile_addressline1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='addressline1',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='addressline2',
        ),
    ]
