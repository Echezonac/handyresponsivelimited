from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields import CharField

# Create your models here.
# Contact models
class Message(models.Model):
  message_name = models.CharField('Username',max_length=100)
  message_email = models.EmailField('User email',max_length=254)
  message_content = models.TextField(max_length=300)
  message_date = models.DateTimeField(auto_now_add=True)
  messageValidator = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  phoneNumber = models.CharField(validators = [messageValidator], max_length = 16, unique = False)
  
  def __str__(self):
    return self.message_name + '-' + self.message_content 
  
# Booking models
class Booking(models.Model):
  client_name = models.CharField('Clientname',max_length=100)
  client_email = models.EmailField('Client email',max_length=254)
  client_message = models.TextField(max_length=300)
  client_message_date = models.DateTimeField(auto_now_add=True)
  messageValidator = RegexValidator(regex = r"^\+?1?\d{8,15}$")
  client_phoneNumber = models.CharField(validators = [messageValidator], max_length = 16, unique = False)
  
  def __str__(self):
    return self.client_name + 'wants' + self.client_message
  
class Hero(models.Model):
  hero_pic = models.ImageField(upload_to='media/pics')
  hero_caption = models.CharField(max_length=100)
  
class About(models.Model):
  pics = models.ImageField(upload_to = 'media/pics')
  banner = models.ImageField(upload_to = 'media/pics')
  
class Service(models.Model):
  icon = models.ImageField(upload_to = 'media/pics')
  banner = models.ImageField(upload_to = 'media/pics')
  caption = models.CharField(max_length=80)
  description = models.TextField(max_length=500)
  
class Testimony(models.Model):
  message = models.TextField(max_length=300)
  name = models.CharField(max_length=20)
  job = models.CharField(max_length=20)
  
class News(models.Model):
  pic = models.ImageField(upload_to='media/pics')
  topic = models.CharField(max_length=80)
  content = models.TextField(max_length=3000)
  post_date = models.DateTimeField(auto_now=True)
  
class Contact(models.Model):
  gmail = models.CharField(max_length=300)
  phone1 = models.CharField(max_length=17)
  phone2 = models.CharField(max_length=17)

class LocationMAp(models.Model):
  googleMap = models.URLField(max_length=10000)
   
class Address(models.Model):
  street = models.CharField(max_length=300)
  city = models.CharField(max_length=300)
  state = models.CharField(max_length=300)
  country = models.CharField(max_length=300)

class Social_Links(models.Model):
   facebook = models.URLField(max_length=1000)
   instagram = models.URLField(max_length=1000)
   twitter = models.URLField(max_length=1000)
   whatsapp = models.URLField(max_length=1000)
  
  