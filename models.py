from django.db import models

# Create your models here.
class product(models.Model):
    live=1
    delete=0
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    deletechoices=((live,'live'),(delete,'delete'))
    deletestatus=models.IntegerField(choices=deletechoices,default=live)
    createdat=models.DateTimeField(auto_now_add=True)
    updatedat=models.DateTimeField(auto_now=True)
    def _str_(self):
        return self.title
