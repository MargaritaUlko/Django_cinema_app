from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Internship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    date = models.DateField()
    experience_required = models.BooleanField(default=False)
    education_required = models.CharField(max_length=100)

    def __str__(self):
        return self.name
