# Generated by Django 4.0.5 on 2022-09-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_UserProfile', '0007_rename_addressline1_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='UserProfile/profile.png', upload_to='UserProfile/'),
        ),
    ]
