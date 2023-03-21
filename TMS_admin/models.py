from django.db import models

# Create your models here.
class Adminlog(models.Model):
    admin_name = models.TextField(max_length=100)
    admin_pass = models.TextField(max_length=100)

class Managerlist(models.Model):
    man_name = models.TextField(max_length=50)
    man_email = models.TextField(max_length=50)
    man_contact = models.TextField(max_length=50)
    man_turfname = models.TextField(max_length=50)
    man_turfloc = models.TextField(max_length=50)
    man_username = models.TextField(max_length=50)
    man_password = models.TextField(max_length=50)
    man_status = models.TextField(max_length=50)    
    turf_desc = models.TextField(max_length=500, null=True)
    turf_cost = models.TextField(max_length=50, null=True)

class Userlist(models.Model):
    user_name = models.TextField(max_length=50)
    user_email = models.TextField(max_length=50)
    user_mobile = models.TextField(max_length=50)
    user_username = models.TextField(max_length=50)
    user_password = models.TextField(max_length=50)
    user_confpassword = models.TextField(max_length=50)    

class Turfimages(models.Model):
    manager_id = models.ForeignKey(Managerlist, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')