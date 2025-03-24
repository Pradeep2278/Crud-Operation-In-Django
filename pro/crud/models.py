from django.db import models

# class pradeep (models.Model):
#     name=models.CharField(max_length=100)
#     age=models.IntegerField(null=False)
#     phone_number=models.IntegerField(null=False)
    
#     def __str__(self):
#         return self.title


class Datas(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(null=False)
    Email=models.EmailField(null=False)


    def __str__(self):
         return self.Name