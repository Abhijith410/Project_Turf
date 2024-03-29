# Generated by Django 4.1.3 on 2023-03-29 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "TMS_admin",
            "0007_alter_adminlog_admin_name_alter_adminlog_admin_pass_and_more",
        ),
        ("TMS_user", "0013_remove_bookings_mn_id_remove_bookings_us_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedbacks",
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
                ("f_name", models.TextField(db_column="name", max_length=50)),
                ("f_email", models.TextField(db_column="email", max_length=50)),
                ("f_contact", models.TextField(db_column="contact", max_length=50)),
                ("f_message", models.TextField(db_column="msg", max_length=100)),
            ],
            options={
                "db_table": "feedbacks",
            },
        ),
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
                ("r_name", models.TextField(db_column="name", max_length=50)),
                ("r_contact", models.TextField(db_column="contact", max_length=50)),
                ("r_message", models.TextField(db_column="msg", max_length=100)),
                (
                    "m_id",
                    models.ForeignKey(
                        db_column="turfid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TMS_admin.managerlist",
                    ),
                ),
                (
                    "u_id",
                    models.ForeignKey(
                        db_column="userid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TMS_admin.userlist",
                    ),
                ),
            ],
            options={
                "db_table": "reviews",
            },
        ),
        migrations.CreateModel(
            name="Bookings",
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
                ("b_name", models.TextField(db_column="name", max_length=50)),
                ("b_contact", models.TextField(db_column="contact", max_length=20)),
                ("b_turf", models.TextField(db_column="turf", max_length=50)),
                ("b_cost", models.TextField(db_column="cost", max_length=10)),
                ("b_date", models.DateField(db_column="date")),
                ("b_tst", models.TimeField(db_column="timefrom")),
                ("b_tend", models.TimeField(db_column="timeto")),
                ("b_tcost", models.TextField(db_column="tcost", max_length=10)),
                ("b_status", models.TextField(db_column="status", max_length=50)),
                ("b_pstatus", models.TextField(db_column="payment", max_length=50)),
                (
                    "mn_id",
                    models.ForeignKey(
                        db_column="mngid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TMS_admin.managerlist",
                    ),
                ),
                (
                    "us_id",
                    models.ForeignKey(
                        db_column="userid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="TMS_admin.userlist",
                    ),
                ),
            ],
            options={
                "db_table": "bookings",
            },
        ),
    ]
