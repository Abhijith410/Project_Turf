# Generated by Django 4.1.3 on 2023-03-21 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("TMS_admin", "0006_managerlist_turf_cost"),
        ("TMS_user", "0007_delete_turfreview"),
    ]

    operations = [
        migrations.CreateModel(
            name="Turfreview",
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
                ("r_name", models.TextField(max_length=50)),
                ("r_contact", models.TextField(max_length=50)),
                ("r_message", models.TextField(max_length=100)),
                (
                    "m_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TMS_admin.managerlist",
                    ),
                ),
                (
                    "u_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TMS_admin.userlist",
                    ),
                ),
            ],
        ),
    ]
