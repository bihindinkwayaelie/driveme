from django.db import models

# Create your models here.

class Driver(models.Model):
    fullname= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    genderchoice =[
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]
    gender= models.CharField(max_length=10,choices=genderchoice)
    dob= models.DateField(null=True)
    phonenumber= models.CharField(max_length=20)
    telephone= models.CharField(max_length=20, default='078')
    address = models.CharField(max_length=30, default='')
    placeofbirth= models.CharField(max_length=50)
    nationality= models.CharField(max_length=20)
    languages= models.CharField(max_length=50)
    experienceskills= models.CharField(max_length=200)
    workingtimechoice =[
    ('Day', 'Day'),
    ('Night', 'Night'),
]
    workingtime= models.CharField(max_length=50, choices=workingtimechoice, null= True)
    idcard= models.FileField(upload_to="driverdocs/IdFolder")
    licensecard= models.FileField(upload_to="driverdocs/LicenseFolder")
    approved = models.BooleanField ('Approved',default=False)
    working = models.BooleanField('Working',default=False)
    created  =  models.DateTimeField(auto_now_add=True, null=True)
    
class Client(models.Model):
    fullname= models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    phonenumber= models.CharField(max_length=20)
    address= models.CharField(max_length=30)
    currentlocation= models.CharField(max_length=30)
    starttime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    endtime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    served = models.BooleanField('Served',default=False)
    created  =  models.DateTimeField(auto_now_add=True, null=True)