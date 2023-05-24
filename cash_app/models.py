from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    date_time = models.DateTimeField('Date')
    amount =  models.IntegerField('Amount')
    info = models.CharField('Info', max_length=100)
    type = models.CharField('Type', max_length=10)

