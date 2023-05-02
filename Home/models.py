from django.db import models
# Create your models here.
class Calculation(models.Model):
    num1 = models.FloatField(max_length=3)
    num2 = models.FloatField(max_length=3)
    operator = models.CharField(max_length=1)
    result = models.FloatField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.num1} {self.operator} {self.num2} = {self.result}"
    
from django.db import models

class Pollutant(models.Model):
    name = models.CharField(max_length=100)
    concentration = models.FloatField()
    background = models.FloatField()

    