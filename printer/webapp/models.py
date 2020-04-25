from django.db import models
class services(models.Model):
    servicename=models.TextField()
class brands(models.Model):
    brandname=models.TextField()
    brandimage=models.ImageField(upload_to="static/img/brands")
class product(models.Model):
    productname=models.CharField(max_length=100)
    subtitle=models.TextField()
    desc=models.TextField()
    brand=models.ForeignKey(brands,null=True,on_delete=models.SET_NULL)
    services=models.ForeignKey(services,null=True,on_delete=models.SET_NULL)
    featured=models.BooleanField(default=False)
    popular=models.BooleanField(default=False)
    
class productImage(models.Model):
    productname=models.ForeignKey(product,on_delete=models.CASCADE),
    image=models.ImageField(upload_to= 'static/img/products')
