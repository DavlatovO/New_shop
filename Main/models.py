from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya", unique=True)
    slug =  models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    price = models.FloatField()
    image = models.ImageField(upload_to='media/')
    quantity = models.IntegerField(default=0)
    slug= models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.name


