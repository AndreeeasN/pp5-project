from django.shortcuts import render


def view_cart(request):
    """
    View that displays the contents of the shopping cart
    """
    return render(request, 'cart/cart.html')
