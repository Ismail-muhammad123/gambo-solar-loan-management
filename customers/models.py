from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Customer(models.Model):
    fullName = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=15)
    alternatePhoneNumber = models.CharField(max_length=10, blank=True)
    email= models.EmailField(blank=True)
    alternate_email = models.EmailField(blank=True)
    nin = models.CharField(max_length=20)
    address = models.TextField()
    bvn = models.CharField(blank=True, max_length=20)
    date_date = models.DateField(auto_now_add=True)
    passport_photo = models.ImageField(upload_to="passport_pictures", blank=True)

    def __str__(self):
        return self.fullName +" - " + self.user.username +" - "+ self.phoneNumber


class Guarantor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    relationship = models.CharField(max_length=100)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='guarantors')

    def __str__(self):
        return self.name
