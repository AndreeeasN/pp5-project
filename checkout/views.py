from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .models import OrderLineItem, Order
from .forms import OrderForm
from cart.contexts import cart_contents
from products.models import Product, ProductVariant

import stripe


def checkout(request):
    """
    Handles cart checkout
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'country': request.POST['country'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'phone_number': request.POST['phone_number'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_key, item_data in cart.items():
                try:
                    product = Product.objects.get(
                        id=item_data['item_id']
                        )
                    product_variant = ProductVariant.objects.get(
                            id=item_data['variant_id']
                            ) if item_data['variant_id'] else None

                    quantity = int(item_data['quantity'])

                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        product_variant=product_variant,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your cart wasn't found in our \
                        database. Please contact site owner for assistance!"
                        )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
                )
        else:
            messages.error(
                request,
                "There was an error processing your form. \
                Please ensure the entered information is valid."
            )
    else:
        if not cart:
            messages.error(
                request,
                "There's currently nothing in your cart."
                )
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing. \
                Did you forget to set it in your environment?"
                )
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Deletes current cart
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)