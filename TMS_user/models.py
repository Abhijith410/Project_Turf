from django.db import models
from TMS_admin.models import *

# Create your models here.
class Feedbacks(models.Model):
    f_name = models.TextField(max_length=50)
    f_email = models.TextField(max_length=50)
    f_contact = models.TextField(max_length=50)
    f_message = models.TextField(max_length=100)

class Turfreview(models.Model):
    u_id = models.ForeignKey(Userlist, on_delete=models.CASCADE)
    m_id = models.ForeignKey(Managerlist, on_delete=models.CASCADE)
    r_name = models.TextField(max_length=50)
    r_contact = models.TextField(max_length=50)
    r_message = models.TextField(max_length=100, null=False)   

    