# Generated by Django 4.2.7 on 2023-11-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="update_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]