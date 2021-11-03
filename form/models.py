from django.db import models


class RegForm(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Mobile_Number = models.PositiveBigIntegerField()
    Email_ID = models.EmailField()
    Department = models.CharField(max_length=200)
    College_Name = models.CharField(max_length=200)
    Last_Modified = models.DateTimeField(auto_now_add=True)
