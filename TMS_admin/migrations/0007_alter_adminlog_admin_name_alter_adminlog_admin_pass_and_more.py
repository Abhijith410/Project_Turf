# Generated by Django 4.1.3 on 2023-03-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("TMS_admin", "0006_managerlist_turf_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminlog",
            name="admin_name",
            field=models.TextField(db_column="name", max_length=50),
        ),
        migrations.AlterField(
            model_name="adminlog",
            name="admin_pass",
            field=models.TextField(db_column="pswd", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_contact",
            field=models.TextField(db_column="contact", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_email",
            field=models.TextField(db_column="email", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_name",
            field=models.TextField(db_column="name", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_password",
            field=models.TextField(db_column="pswd", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_status",
            field=models.TextField(db_column="status", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_turfloc",
            field=models.TextField(db_column="loc", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_turfname",
            field=models.TextField(db_column="turf", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="man_username",
            field=models.TextField(db_column="usnam", max_length=50),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="turf_cost",
            field=models.TextField(db_column="cost", max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="managerlist",
            name="turf_desc",
            field=models.TextField(db_column="desc", max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="turfimages",
            name="images",
            field=models.ImageField(db_column="images", upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="turfimages",
            name="manager_id",
            field=models.ForeignKey(
                db_column="m_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="TMS_admin.managerlist",
            ),
        ),
        migrations.AlterField(
            model_name="userlist",
            name="user_confpassword",
            field=models.TextField(db_column="cpswd", max_length=50),
        ),
        migrations.AlterField(
            model_name="userlist",
            name="user_email",
            field=models.TextField(db_column="email", max_length=50),
        ),
        migrations.AlterField(
            model_name="userlist",
            name="user_mobile",
            field=models.TextField(db_column="mobile", max_length=50),
        ),
        migrations.AlterField(
            model_name="userlist",
            name="user_name",
            field=models.TextField(db_column="name", max_length=50),
        ),
        migrations.AlterField(
            model_name="userlist",
            name="user_password",
            field=models.TextField(db_column="pswd", max_length=50),
        ),
        migrations.AlterField(
            model_name="userlist",
            name="user_username",
            field=models.TextField(db_column="usnam", max_length=50),
        ),
        migrations.AlterModelTable(
            name="adminlog",
            table="adminlogin",
        ),
        migrations.AlterModelTable(
            name="managerlist",
            table="managerlist",
        ),
        migrations.AlterModelTable(
            name="turfimages",
            table="turfimages",
        ),
        migrations.AlterModelTable(
            name="userlist",
            table="userlist",
        ),
    ]