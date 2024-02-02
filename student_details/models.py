from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    Hindi = models.IntegerField()
    Telugu = models.IntegerField()
    English = models.IntegerField()
    Maths = models.IntegerField()
    Science = models.IntegerField()
    Social = models.IntegerField()
    Total_Marks = models.IntegerField()

    def __str__(self):
        return self.name

# Create your models here.
