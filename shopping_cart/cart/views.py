from django.shortcuts import render
from django.views import View
from .models import Order, Cart


class ShoppingCartView(View):
    def get(self, request):
        cart = Cart.objects.first()
        orders = Order.objects.filter(cart=cart)
        context = {
            'orders': orders,
        }
        return render(request, 'cart/shopping_cart.html', context)

    def post(self, request):
        shopping_cart = {}
        for id, quantity in request.POST.items():
            if id != "csrfmiddlewaretoken":
                product = Order.objects.get(pk=id).product
                if self.check_inventory(product, int(quantity)):
                    shopping_cart[product] = int(quantity)
                else:
                    error_message = self.get_error_message(product)
                    context = {
                        'error_message': error_message,
                    }
                    return render(request, 'cart/error.html', context)
        success_message = self.get_success_message()
        context = {
            'success_message': success_message,
        }
        self.update_inventory(shopping_cart)
        return render(request, 'cart/success.html', context)

    def check_inventory(self, product, quantity):
        return product.quantity >= quantity

    def get_error_message(self, product):
        if product.quantity == 0:
            return f"I'm sorry, but we are out of stock for {product.name}."
        return f"I'm sorry, but we only have {product.quantity}kg of {product.name} left."

    def get_success_message(self):
        return f"You have completed your order successfully."

    def update_inventory(self, shopping_cart):
        for product, quantity in shopping_cart.items():
            product.quantity -= quantity
            product.save()
