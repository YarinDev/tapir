# Generated by Django 3.1.13 on 2021-09-23 17:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shifts", "0021_auto_20210920_1808"),
    ]

    operations = [
        migrations.AddField(
            model_name="shift",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="shifttemplate",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="shiftslot",
            name="required_capabilities",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("shift_coordinator", "Shift Coordinator"),
                        ("cashier", "Cashier"),
                        ("member_office", "Member Office"),
                        ("bread_delivery", "Bread Delivery"),
                    ],
                    max_length=128,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="shiftslottemplate",
            name="required_capabilities",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("shift_coordinator", "Shift Coordinator"),
                        ("cashier", "Cashier"),
                        ("member_office", "Member Office"),
                        ("bread_delivery", "Bread Delivery"),
                    ],
                    max_length=128,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="shiftuserdata",
            name="capabilities",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("shift_coordinator", "Shift Coordinator"),
                        ("cashier", "Cashier"),
                        ("member_office", "Member Office"),
                        ("bread_delivery", "Bread Delivery"),
                    ],
                    max_length=128,
                ),
                default=list,
                size=None,
            ),
        ),
    ]
