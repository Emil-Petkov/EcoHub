# Generated by Django 5.1.3 on 2024-12-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="https://eco-hub-bucket.s3.eu-north-1.amazonaws.com/media/profile_pictures/default-profile.jpg",
                null=True,
                upload_to="profile_pictures/",
            ),
        ),
    ]
