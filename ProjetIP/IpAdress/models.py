from django.db import models

class Server(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    ip_adress=models.GenericIPAddressField(protocol='both')
    def __str__(self):
        return self.name
    
class Command (models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class IP (models.Model):
    id=models.AutoField(primary_key=True)
    number= models.CharField(max_length = 15)
    