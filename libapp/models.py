from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250 , blank=True , null=True)
    author_image = models.ImageField(upload_to='photos' ,blank=True , null=True )
    book_image = models.ImageField(upload_to='photos' ,blank=True , null=True )
    pages= models.IntegerField(blank=True , null=True)
    price=models.DecimalField(max_digits=5 , decimal_places=2,blank=True , null=True)
    rental_price_per_day = models.DecimalField(max_digits=5 , decimal_places=2,blank=True , null=True)
    book_status = models.CharField(max_length=50, choices=[("available","available"),("sold","sold"),("rented","rented")] , null=True , blank=True)
    rental_period = models.IntegerField(blank=True , null=True)
    activity = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT , null=True , blank=True)
    def __str__(self):
        return self.title