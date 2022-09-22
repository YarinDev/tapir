# Generated by Django 3.2.15 on 2022-09-18 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coop", "0030_newmembersandsharesemailrecaplogs"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExtraSharesForAccountingRecap",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_shares", models.PositiveIntegerField()),
                ("date", models.DateField()),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="coop.shareowner",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewMembershipsForAccountingRecap",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number_of_shares", models.PositiveIntegerField()),
                ("date", models.DateField()),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="coop.shareowner",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="NewMembersAndSharesEmailRecapLogs",
        ),
    ]
