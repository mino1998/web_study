from django.db import models

# Create your models here.
class Item(models.Model):
    itemID=models.CharField(max_length=50, primary_key=True)
    itemName=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    pirctureURL=models.CharField(max_length=200)