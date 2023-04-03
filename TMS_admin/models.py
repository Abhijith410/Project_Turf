from django.db import models

# Create your models here.
class Adminlog(models.Model):
    admin_name = models.TextField(max_length=50, db_column='name')
    admin_pass = models.TextField(max_length=50, db_column='pswd')

    class Meta:
        db_table="adminlogin"	

class Managerlist(models.Model):
    man_name = models.TextField(max_length=50, db_column='name')
    man_email = models.TextField(max_length=50, db_column='email')
    man_contact = models.TextField(max_length=50, db_column='contact')
    man_turfname = models.TextField(max_length=50, db_column='turf')
    man_turfloc = models.TextField(max_length=50, db_column='loc')
    man_username = models.TextField(max_length=50, db_column='usnam')
    man_password = models.TextField(max_length=50, db_column='pswd')
    man_status = models.TextField(max_length=50, db_column='status')    
    turf_desc = models.TextField(max_length=500, null=True, db_column='desc')
    turf_cost = models.TextField(max_length=50, null=True, db_column='cost')

    class Meta:
        db_table="managerlist"

class Userlist(models.Model):
    user_name = models.TextField(max_length=50, db_column='name')
    user_email = models.TextField(max_length=50, db_column='email')
    user_mobile = models.TextField(max_length=50, db_column='mobile')
    user_username = models.TextField(max_length=50, db_column='usnam')
    user_password = models.TextField(max_length=50, db_column='pswd')
    user_confpassword = models.TextField(max_length=50, db_column='cpswd')    

    class Meta:
        db_table="userlist"

class Turfimages(models.Model):
    manager_id = models.ForeignKey(Managerlist, on_delete=models.CASCADE, db_column='m_id')
    images = models.ImageField(upload_to='images/', db_column='images')

    class Meta:
        db_table="turfimages"