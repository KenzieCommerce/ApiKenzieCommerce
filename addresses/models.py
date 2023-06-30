from django.db import models

class Address(models.Model):
    street_name = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    number = models.IntegerField()
    zip_code = models.IntegerField()

   
   
