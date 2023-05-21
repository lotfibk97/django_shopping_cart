from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Cart(models.Model):
    price = models.PositiveIntegerField(default=0, null=False)
    completed = models.BooleanField(default=False)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.product}"
