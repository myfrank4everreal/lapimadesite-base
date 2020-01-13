from django.db import models

class Products(models.Model):
    img = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=300)
    price = models.FloatField(default=1)
    amz_link = models.CharField(max_length=300, null=True, blank=True)
    

    def __str__(self):
        return self.name

    
    def shotend_desc(self):
        return self.desc[:200] + '...'
   