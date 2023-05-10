from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=40)
    price = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
