# Generated by Django 4.1.4 on 2023-01-09 17:04

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
    ]