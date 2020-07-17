import os
import stripe
from flask import Flask, jsonify, render_template, request, abort
from Transactions import *

print("Running " + os.path.basename(__file__))

app = Flask(__name__)

stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

size = 100

start = time.time()
print("uploading products and prices...")
for i in range(len(products[:size])):
    product = stripe.Product.create(
        id = "prod_" + product_dict['product_id'][i],
        name = product_dict['product_category_name'][i],
        attributes = ['product_weight_g','product_length_cm',
                    'product_height_cm','product_width_cm'],
        type='good'
    )
    item = list(item_dict['product_id'].values()).index(product_dict['product_id'][i])
    if product_dict['product_id'][i] in item_dict['product_id'].values():
        price = stripe.Price.create(
            product = "prod_" + product_dict['product_id'][i],
            unit_amount = int(item_dict['price'][item]*100),
            currency = 'BRL'
        )
end = time.time()
print("upload finished in " + str(round(end-start, 2)) + " seconds")

start = time.time()
print("uploading customers and cards...")
existing = [] # delete
for i in range(len(customers[:size])):
    existing.append(customer_dict['customer_id'][i]) # delete
    customer = stripe.Customer.create(
        id = "cus_" + customer_dict['customer_id'][i],
        name = customer_dict['customer_name'][i],
        email = customer_dict['customer_name'][i].split()[0] + "." + \
                customer_dict['customer_name'][i].split()[1] + "@email.com",
        metadata = {"customer_city": customer_dict['customer_city'][i],
                  "customer_state": customer_dict['customer_state'][i],
                  "customer_zip_code_prefix":
                  customer_dict['customer_zip_code_prefix'][i]}       
    )
    stripe.Customer.create_source(
      "cus_" + customer_dict['customer_id'][i],
      source="tok_visa",
    )
end = time.time()
print("upload finished in " + str(round(end-start, 2)) + " seconds")

start = time.time()
print("uploading charges...")
for item in range(len(items[:size])):
    j = list(order_dict['customer_id'].values()).index(existing[item]) # delete
    i = list(item_dict['order_id'].values()).index(order_dict['order_id'][j]) # delete
    charge = stripe.Charge.create(
        currency = 'BRL',
        amount = int(item_dict['price'][i]*100),
        customer = "cus_" + orders[orders['order_id'] == item_dict['order_id'][i]]['customer_id'].to_list()[0]
    )
end = time.time()
print("upload finished in " + str(round(end-start, 2)) + " seconds")
