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
   

class BusinesZone(models.Model):
    img = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=300)
    desc = models.TextField(max_length=3000, null=True, blank=True)
    price = models.FloatField(default=1)
    amz_link = models.CharField(max_length=300, null=True, blank=True)
    
    
    def __str__(self):
        return self.name

    def shotend_desc(self):
        return self.desc[:200] + '...'


class GameZone(models.Model):
    img = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=400)
    desc = models.TextField(max_length=3000, null=True, blank=True)
    price = models.FloatField(default=1)
    amz_link = models.CharField(max_length=300, null=True, blank=True)
    
    
    def __str__(self):
        return self.name

    def shotend_desc(self):
        return self.desc[:200] + '...'

    

class GigZone(models.Model):
    img = models.FileField(null=True, blank=True)
    name = models.CharField(max_length=400)
    desc = models.TextField(max_length=3000, null=True, blank=True)
    price = models.FloatField(default=1)
    amz_link = models.CharField(max_length=300, null=True, blank=True)
    
    
    def __str__(self):
        return self.name

    
    def shotend_desc(self):
        return self.desc[:200] + '...'
