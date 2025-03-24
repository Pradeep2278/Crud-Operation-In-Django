from django.db import models

class Datas(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(null=False)
    Email=models.EmailField(null=False)


    def __str__(self):
         return self.Name
