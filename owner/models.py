from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class Owner(models.Model):
    
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'
