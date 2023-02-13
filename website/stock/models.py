from django.db import models

class Stockdata(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Tradedata(models.Model):
    code=models.CharField(max_length=100,null=True)
    action=models.CharField(max_length=100)
    sname=models.CharField(max_length=200)
    sprice=models.IntegerField()
    sqty=models.IntegerField()

    class Meta:
        db_table='dataa'

    def __str__(self):
        return f"{self.action} {self.sname}"
