# Generated by Django 5.1.3 on 2024-12-10 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0014_alter_customuser_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="profile_picture",
        ),
    ]
