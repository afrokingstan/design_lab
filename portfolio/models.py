from django.db import models
from products.models import Category
from profiles.models import UserProfile
from checkout.models import Order


# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
