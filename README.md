django-paypal-recurring
=======================

Django PayPal Recurring is an app for Django Framework to offer subscription using Express Checkout https://developer.paypal.com/docs/classic/express-checkout/ht_ec-recurringPaymentProfile-curl-etc/

Usage
=====

1.  'subscription' in INSTALLED_APPS
2.  Fill these settings:

    PAYPAL_API_USERNAME = 'xxxxx'
    
    PAYPAL_API_PASSWORD = 'xxxxx'
    
    PAYPAL_API_SIGNATURE = 'xxxx'
    
    PAYPAL_SANDBOX_MODE = True
    
    SITE_CURRENCY = 'EUR'
