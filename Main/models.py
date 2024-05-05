from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser



class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya", unique=True)
    slug =  models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    price = models.FloatField()
    image = models.ImageField(upload_to='media/')
    quantity = models.IntegerField(default=0)
    slug= models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Review(models.Model):
    mark = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    text = models.TextField()
    


