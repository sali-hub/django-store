from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Order(models.Model):
    adress = models.TextField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.user)