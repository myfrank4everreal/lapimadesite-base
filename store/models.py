from django.db import models

class Products(models.Model):
    img = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=300)
    price = models.FloatField(default=1)
    imagelink = models.CharField(max_length=300, null=True, blank=True)
    productlink = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.name    

