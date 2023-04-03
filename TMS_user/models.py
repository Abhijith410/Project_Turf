from django.db import models
from TMS_admin.models import *

# Create your models here.

class Feedbacks(models.Model):
    f_name = models.TextField(max_length=50,db_column='name')
    f_email = models.TextField(max_length=50,db_column='email')
    f_contact = models.TextField(max_length=50, db_column='contact')
    f_message = models.TextField(max_length=100, db_column='msg')

    class Meta:
        db_table="feedbacks"

class Turfreview(models.Model):
    u_id = models.ForeignKey(Userlist, on_delete=models.CASCADE, db_column='userid')
    m_id = models.ForeignKey(Managerlist, on_delete=models.CASCADE, db_column='turfid')
    r_name = models.TextField(max_length=50, db_column='name')
    r_contact = models.TextField(max_length=50, db_column='contact')
    r_message = models.TextField(max_length=100, null=False, db_column='msg')   

    class Meta:
        db_table="reviews"

class Bookings(models.Model):
    us_id = models.ForeignKey(Userlist, on_delete=models.CASCADE, db_column='userid')    
    mn_id = models.ForeignKey(Managerlist, on_delete=models.CASCADE, db_column='mngid') 
    b_name = models.TextField(max_length=50, db_column='name')
    b_contact = models.TextField(max_length=20, db_column='contact')
    b_turf = models.TextField(max_length=50, db_column='turf')
    b_cost = models.TextField(max_length=10, db_column='cost')
    b_date = models.DateField(db_column='date')
    b_tst = models.TimeField(db_column='timefrom')
    b_tend = models.TimeField(db_column='timeto')
    b_tcost = models.TextField(max_length=10, db_column='tcost')
    b_status = models.TextField(max_length=50, db_column='status')
    b_pstatus = models.TextField(max_length=50, db_column='payment')

    class Meta:
        db_table="bookings"