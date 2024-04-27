from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class customer(models.Model):
    live=0
    delete=0
    deletechoices=((live,'live'),(delete,'delete'))
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=700)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer profile+')
    phone=models.CharField(max_length=30)
    deletestatus=models.IntegerField(choices=deletechoices,default=live)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now_add=True)
    def _str_(self)->str:
        return self.title
        

