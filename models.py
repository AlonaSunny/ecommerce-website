from django.db import models


# Create your models here.
from customers.models import customer
from product.models import product

# Create your models here.
class Order(models.Model):
    live=0
    delete=0
    deletechoices=((live,'live'),(delete,'delete'))
    cartstage=1
    orderconfirmed=1
    orderrejected=4
    orderprocessed=2
    orderdelivered=3
    statuschoice=((orderprocessed,"orderprocessed"),
                  (orderdelivered,"orderdelivered"),
                  (orderrejected,"orderrejected"))

    
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    deletestatus=models.IntegerField(choices=deletechoices,default=live)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now_add=True)
    class ordereditem(models.Model):
        product=models.ForeignKey(product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
        quantity=models.IntegerField(default=1)
        owner=models.ForeignKey('order.Order',on_delete=models.CASCADE,related_name='orderitem')
