from django.db import models

# Create your models here.
class Account_Details(models.Model):
    First_name = models.CharField(max_length = 30)
    Last_name = models.CharField(max_length = 30)
    Emails = models.CharField(max_length = 30)
    Contact_no = models.CharField(max_length = 10)
    Address = models.TextField()
    def __str__(self):
        return self.First_name