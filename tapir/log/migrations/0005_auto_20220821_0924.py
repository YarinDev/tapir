# Generated by Django 3.2.15 on 2022-08-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("log", "0004_auto_20211003_0941"),
    ]

    operations = [
        migrations.AddField(
            model_name="emaillogentry",
            name="email_id",
            field=models.CharField(default="unknown", max_length=128),
        ),
        migrations.AlterField(
            model_name="emaillogentry",
            name="subject",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
