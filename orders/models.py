from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, default=None)
    adress = models.CharField(max_length=100)
    items = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now=True)

    
    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price

        return total

    def __str__(self):
        return f'Order {self.id} by {self.user}'