# Generated by Django 5.0.2 on 2024-03-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookmarks", "0025_userprofile_search_preferences"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="custom_css",
            field=models.TextField(blank=True),
        ),
    ]