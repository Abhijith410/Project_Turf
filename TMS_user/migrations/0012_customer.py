# Generated by Django 4.1.3 on 2023-03-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TMS_user", "0011_bookings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(db_column="f_name", max_length=30)),
                ("last_name", models.CharField(db_column="l_name", max_length=30)),
                ("mobile", models.CharField(db_column="mob", max_length=12)),
                ("gender", models.CharField(db_column="gender", max_length=6)),
                ("dob", models.DateField(db_column="dob")),
                ("address", models.CharField(db_column="addr", max_length=70)),
                ("country", models.CharField(db_column="cntry", max_length=30)),
                ("user_type", models.CharField(db_column="u_type", max_length=10)),
                ("email", models.CharField(db_column="email", max_length=50)),
                ("passwd", models.CharField(db_column="passwd", max_length=50)),
                ("otp", models.CharField(db_column="otp", max_length=70)),
                (
                    "status",
                    models.CharField(db_column="status", default="", max_length=20),
                ),
            ],
            options={
                "db_table": "customer",
            },
        ),
    ]