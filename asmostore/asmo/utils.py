from .models import *


class CartAuthenticatedUser:
    def __init__(self, request, product_slug=None, action=None, quantity=1):
        self.request = request
        self.quantity = quantity

        if product_slug and action:
            self.add_or_delete(product_slug, action)

    def get_cart_info(self):
        customer, created = Customer.objects.get_or_create(
            user=self.request.user
        )

        order, created = Order.objects.get_or_create(
            customer=customer
        )

        order_products = order.orderproduct_set.all()

        cart_total_price = order.get_cart_total_price
        cart_total_price_shipping = order.get_cart_total_price + 20

        cart_total_quantity = order.get_cart_quantity

        return {
            'order': order,
            'order_products': order_products,
            'cart_total_price': cart_total_price,
            'cart_total_quantity': cart_total_quantity,
            'cart_total_price_shipping': cart_total_price_shipping
        }

    def add_or_delete(self, product_slug, action):
        order = self.get_cart_info()['order']
        product = Product.objects.get(slug=product_slug)
        order_product, created = OrderProduct.objects.get_or_create(
            order=order,
            product=product
        )

        if action == 'add' and product.quantity > 0:
            order_product.quantity += self.quantity
            product.quantity -= self.quantity

        if action == 'delete':
            order_product.quantity -= self.quantity
            product.quantity += self.quantity

        order_product.save()
        product.save()

        if order_product.quantity <= 0:
            order_product.delete()
