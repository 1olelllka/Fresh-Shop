from .models import Cart, ProductOrder

def get_cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        items = ProductOrder.objects.filter(cart__in=cart)
        count = ProductOrder.objects.filter(cart__in=cart).count()
        return locals()
    else:
        items = ProductOrder.objects.none()
        return locals()