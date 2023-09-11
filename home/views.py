from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse


def index(request):
    """
    View that displays the index page
    """
    return render(request, 'home/index.html')


def newsletter_signup(request):
    """
    Sends out a confirmation email to provided email address.
    Note that no real newsletter exists and as such lacks functionality.
    """
    customer_email = request.POST.get('email')
    seasonal_promotions = request.POST.get('promotions')

    subject = render_to_string(
        'home/confirmation_emails/confirmation_email_subject.txt')
    body = render_to_string(
        'home/confirmation_emails/confirmation_email_body.txt',
        {
            'seasonal_promotions': seasonal_promotions,
            'customer_email': customer_email,
            'contact_email': settings.DEFAULT_FROM_EMAIL,
        })

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email]
    )

    printMsg = f'Thank you for signing up for our newsletter! \
        A confirmation email has been sent to {customer_email}'

    messages.success(request, printMsg)

    return redirect(reverse('home'))
