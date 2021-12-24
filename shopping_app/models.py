from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse("shopping_app:prod_cat", args=[self.slug])



    def __str__(self):
        return '{}'.format(self.name)




class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField()

    def get_url(self):
        return reverse("shopping_app:ProdCatDetail", args=[self.category.slug, self.slug])

