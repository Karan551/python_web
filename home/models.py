from django.db import models


# Create your models here.
class Contact(models.Model):
    serial_number = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=250)
    user_email = models.CharField(max_length=100)
    user_phoneNumber = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
