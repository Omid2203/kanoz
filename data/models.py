from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

class Part(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Branch(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=40, blank=False)
    cellphone = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=35)
    publish = models.DateTimeField(default=timezone.now)
    document = models.FileField(blank=True, upload_to='media')
    part = models.ForeignKey(Part, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
