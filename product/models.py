from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_count')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_review')
    stars = models.IntegerField()

    def __str__(self):
        return self.text