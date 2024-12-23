# Generated by Django 5.1.3 on 2024-12-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_customuser_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="users/profile_pictures/default-profile.jpg",
                null=True,
                upload_to="profile_pictures/",
            ),
        ),
    ]
