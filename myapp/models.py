from django.db import models

class Studentdetail(models.Model):
    Id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    dob = models.DateField()
    nationality = models.CharField(max_length=20)
    email = models.EmailField()
    institute = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.name

