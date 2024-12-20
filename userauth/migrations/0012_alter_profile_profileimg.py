# Generated by Django 5.1.2 on 2024-11-04 12:23

import socialmedia.settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0011_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', storage=socialmedia.settings.ProfilePictureStorage(), upload_to=''),
        ),
    ]
