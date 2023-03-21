from django.db import models

# Create your models here.
class Feedbacks(models.Model):
    f_name = models.TextField(max_length=50)
    f_email = models.TextField(max_length=50)
    f_contact = models.TextField(max_length=50)
    f_message = models.TextField(max_length=100)