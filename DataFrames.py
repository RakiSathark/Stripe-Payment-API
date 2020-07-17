import pandas as pd
pd.set_option('display.max_columns', None) # show all column values
from os import listdir
from os.path import isfile, join

mypath = "Brazilian_E-Commerce_Dataset/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    df = pd.read_csv("Brazilian_E-Commerce_Dataset/" + file)
    print(file)
    print(list(df.columns))
    print(df.head(5))
    print(str(df.shape) + '\n')

customers = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_customers_dataset.csv")
locations = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_geolocation_dataset.csv")
orders = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_orders_dataset.csv")
items = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_order_items_dataset.csv")
payments = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_order_payments_dataset.csv")
reviews = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_order_reviews_dataset.csv")
products = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_products_dataset.csv")
sellers = pd.read_csv("Brazilian_E-Commerce_Dataset/olist_sellers_dataset.csv")
names = pd.read_csv("Brazilian_E-Commerce_Dataset/product_category_name_translation.csv")