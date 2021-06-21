from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Transfer(models.Model):
    # ID=models.IntegerField()
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Balance=models.IntegerField()

    def __str__(self):
        return f"{self.Name}"

class History(models.Model):
    # ID=models.IntegerField()
    Sender=models.CharField(max_length=100)   
    Receiver=models.CharField(max_length=100)   
    Amount=models.IntegerField()
    dateandtime=DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.Sender}"



