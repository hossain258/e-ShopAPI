# Generated by Django 4.0.5 on 2022-09-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_UserProfile', '0008_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.CharField(default=1, max_length=25, unique=True),
            preserve_default=False,
        ),
    ]