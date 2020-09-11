from django.db import models

# Create your models here.

class ConvertBinary(models.Model):
    hex_input = models.CharField(max_length = 400)
    hex_input2 = models.CharField(max_length = 400)


