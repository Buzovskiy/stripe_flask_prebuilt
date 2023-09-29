#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51NuCZ1ABhNwAdaFhQYv4Bc73R3P3VZ34jIfPzgOACUBGBtUQbfiuq4Jj687dwpIydCJcNBSZdp2RDrvGhBKOsAeO00p72j8xu9'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:3000'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        # Create product
        product = stripe.Product.create(name="Order 1")

        price = stripe.Price.create(
            unit_amount=2005,
            currency="eur",
            product=product.id,
        )

        checkout_session = stripe.checkout.Session.create(
            line_items=[{'price': price.id, 'quantity': 1}],
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
            automatic_tax={'enabled': True},
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)