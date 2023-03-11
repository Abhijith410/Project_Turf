# Generated by Django 4.1.3 on 2023-03-06 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TMS_admin", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Managerlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("man_name", models.TextField(max_length=50)),
                ("man_email", models.TextField(max_length=50)),
                ("man_contact", models.TextField(max_length=50)),
                ("man_turfname", models.TextField(max_length=50)),
                ("man_turfloc", models.TextField(max_length=50)),
                ("man_username", models.TextField(max_length=50)),
                ("man_password", models.TextField(max_length=50)),
                ("man_status", models.TextField(max_length=50)),
            ],
        ),
    ]
