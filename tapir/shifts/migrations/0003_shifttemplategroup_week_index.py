# Generated by Django 3.1.8 on 2021-05-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shifts", "0002_auto_20210521_0832"),
    ]

    operations = [
        migrations.AddField(
            model_name="shifttemplategroup",
            name="week_index",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
