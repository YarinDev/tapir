# Generated by Django 3.1.7 on 2021-04-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0002_auto_20210406_1431"),
    ]

    operations = [
        migrations.AlterField(
            model_name="draftuser",
            name="num_shares",
            field=models.IntegerField(
                default=1, editable=False, verbose_name="Number of Shares"
            ),
        ),
    ]
