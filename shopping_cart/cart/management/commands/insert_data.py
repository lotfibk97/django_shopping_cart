from django.core.management.base import BaseCommand
from django.utils import timezone
from cart.models import Product, Cart, Order


class Command(BaseCommand):
    help = 'Inserts sample data into the models'

    def handle(self, *args, **options):
        # Create Products
        potatoes = Product.objects.create(name='Potatoes', quantity=2, price=5)
        carrots = Product.objects.create(name='Carrots', quantity=1, price=4)
        onions = Product.objects.create(name='Onions', quantity=1, price=2)

        # Create Cart
        cart = Cart.objects.create(price=0, completed=False)

        # Create Orders
        order1 = Order.objects.create(
            product=potatoes, quantity=2, timestamp=timezone.now(), cart=cart)
        order2 = Order.objects.create(
            product=carrots, quantity=1, timestamp=timezone.now(), cart=cart)
        order3 = Order.objects.create(
            product=onions, quantity=1, timestamp=timezone.now(), cart=cart)

        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))
