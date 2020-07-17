import time
import pandas as pd

products = pd.read_csv("Brazilian_E-Commerce_Dataset\olist_products_dataset.csv")
trans = pd.read_csv("Brazilian_E-Commerce_Dataset\product_category_name_translation.csv")
product_dict = products.to_dict()

print("starting name conversion...")
start = time.time()
i = 0
for prod in product_dict['product_category_name'].values():
    try:
        product_dict['product_category_name'][i] = trans[trans["product_category_name"] == prod]["product_category_name_english"].to_list()[0]
    except:
        pass
    i += 1
print("product names converted")
end = time.time()
print("conversion finished in " + str(round(end - start, 2)) + " seconds")

products = pd.DataFrame.from_dict(product_dict)
products.to_csv("olist_products_dataset.csv", index=False)
