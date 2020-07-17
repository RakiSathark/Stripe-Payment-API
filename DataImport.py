import pandas as pd
pd.set_option('display.max_columns', None) # show all column values
import os
import time
import names
from os import listdir
from os.path import isfile, join
from pymongo import MongoClient

print("Running " + os.path.basename(__file__))

def connect_mongodb(host, port, db, username, password):
    """A method for making a connection to MongoDB"""
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]

def read_mongodb(db, collection, query={}, host='localhost', port=27017, username=None, password=None, id_null=True):
    """Read data from MongoDB and store into a dataframe"""
    # Connect to MongoDB
    db = connect_mongodb(host=host, port=port, db=db, username=username, password=password)
    # Create a query for the specific database and collection
    cursor = db[collection].find(query)
    # Expand cursor and construct the dataframe
    df =  pd.DataFrame(list(cursor))
    # Delete the _id value
    if id_null:
        del df['_id']
    return df

print("starting data import...")
start = time.time()
customers = read_mongodb('payment','customers')
locations = read_mongodb('payment','location')
orders = read_mongodb('payment','orders')
items = read_mongodb('payment','items')
payments = read_mongodb('payment','payments')
reviews = read_mongodb('payment','reviews')
products = read_mongodb('payment','products')
sellers = read_mongodb('payment','sellers')
trans = read_mongodb('payment','translations')
end = time.time()
print("import finished in " + str(round(end - start, 2)) + " seconds")

products = products.drop(products[products['product_category_name'] == ''].index).reset_index()
items = items[items['price'] >= 2].reset_index() # filter out products less than USD $0.50
products = products[products['product_id'].isin(list(items['product_id']))].reset_index()
orders = orders[orders['order_id'].isin(list(items['order_id']))].reset_index()
customers = customers[customers['customer_id'].isin(list(orders['customer_id']))].reset_index()

print("starting dataframe conversion to dictionary...")
start = time.time()
customer_dict = pd.DataFrame(customers).to_dict()
location_dict = pd.DataFrame(locations).to_dict()
order_dict = pd.DataFrame(orders).to_dict()
item_dict = pd.DataFrame(items).to_dict()
payment_dict = pd.DataFrame(payments).to_dict()
review_dict = pd.DataFrame(reviews).to_dict()
product_dict = pd.DataFrame(products).to_dict()
seller_dict = pd.DataFrame(sellers).to_dict()
name_dict = pd.DataFrame(trans).to_dict()
end = time.time()
print("conversion finished in " + str(round(end - start, 2)) + " seconds")
