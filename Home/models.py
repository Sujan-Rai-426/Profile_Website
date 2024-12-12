

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

# Create your models here.

# Model class for Contact Setion
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=80, blank=False, null=False)
    message = models.TextField(max_length=500, blank=False, null=False)

# Model class for Project Section
class Project(models.Model):
    # For input type with choice 
    WEBSITE_TYPE_CHOICES = [
        ('Static Website', 'Static Website'),
        ('Dynamic Website', 'Dynamic Website'),
        ('Web Application', 'Web Application'),
        ('Visit Below', 'Visit Below')
    ]
    name = models.CharField(max_length=50, blank=False)
    website_type = models.CharField(max_length=20, choices= WEBSITE_TYPE_CHOICES, default='Static Website')
    detail = models.TextField(max_length = 150, blank=False)
    link = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', folder='media_Profile_website/upload_project_img/', blank=False, null=False)
    # image = models.ImageField(upload_to='Profile_website/upload_project_img/', blank=False, null=False)
    
    def __str__(self):
        return self.name


# Model class for skill section of front end
class Front_End_Skill(models.Model):
    name = models.CharField(max_length=20, blank=False)
    percentage = models.IntegerField (validators=[MinValueValidator(0), MaxValueValidator(100)] ,null=True ,blank=False)
    def __str__(self):
        return self.name


# Model class for skill section of back end
class Back_End_Skill(models.Model):
    name = models.CharField(max_length=20, blank=False)
    percentage = models.IntegerField (validators=[MinValueValidator(0), MaxValueValidator(100)] ,null=True ,blank=False)
    def __str__(self):
        return self.name


# Models for dowmload section for downloading files like resume images and other pdf for user
class Download(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    file = CloudinaryField('file', folder='media_Profile_website/download/', transformation={"format": "jpg"}, blank=False, null=False)
    # file = models.FileField(upload_to='Profile_website/download_file/', blank=False, null=False)
    def __str__(self):
        return self.name


# Model to show my current address of developer class
class CurrentAddress(models.Model):
    location = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.location
    

# Models for the Activements or License and certificates
class Achivements(models.Model):
    image = CloudinaryField('image', folder='media_Profile_website/Achivements_img/', blank=False, null=False)
    link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=False)
    
    def __str__(self):
        return self.name
    