# Generated by Django 4.1.3 on 2023-03-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TMS_admin", "0005_turfimages"),
    ]

    operations = [
        migrations.AddField(
            model_name="managerlist",
            name="turf_cost",
            field=models.TextField(max_length=50, null=True),
        ),
    ]