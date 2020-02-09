from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, null=False)
    desciption = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'
