from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Registration(models.Model):
#     username=models.CharField(max_length=100)
#     firstname=models.CharField(max_length=100)
#     lastname=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     confirm_password = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100)
#     date_of_birth = models.IntegerField
#     district = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     pincode = models.IntegerField
#     upload_image=models.FileField(upload_to= "documents",default="image.jpg")
class Courses(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price = models.IntegerField(default="35000")
    image=models.FileField(upload_to="documents",default="default.jpg")
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    date= models.DateField
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pin = models.IntegerField
    upload_image = models.FileField(upload_to="documents", default="image.jpg")

