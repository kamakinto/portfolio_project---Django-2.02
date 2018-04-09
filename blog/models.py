from django.db import models

class Blog(models.Model):
  image = models.ImageField(upload_to='images/')
  pub_date = models.DateField(auto_now_add=True)
  last_modified = models.DateField(auto_now=True)
  author=models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=400)
  body= models.TextField()

# Create your models here.
