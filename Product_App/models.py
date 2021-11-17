from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from djrichtextfield.models import RichTextField
# Create your models here.

class Catagory (models.Model):

    title = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Product Catagorys"
        verbose_name_plural = "Catagorys"

    def __str__(self):
        return self.title


class Products(models.Model):
    minimage = models.ImageField(upload_to = 'product')
    img1 = models.ImageField(upload_to = 'product',blank=True, null=True)
    more_img = models.BooleanField(default=False)
    img2 = models.ImageField(upload_to = 'product',blank=True, null=True)
    img3 = models.ImageField(upload_to = 'product',blank=True, null=True)
    name = models.CharField(max_length=64)
    catagory = models.ForeignKey(Catagory, on_delete=CASCADE,related_name='catagory')
    preview_text = models.TextField(max_length=264, verbose_name='Preview Text ')
    detail_text = RichTextField(max_length=1000, verbose_name='Descriptions')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    crate_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    class Meta:
        ordering = ['-crate_date']
        # verbose_name = 'Products'
        verbose_name_plural = 'Products'
