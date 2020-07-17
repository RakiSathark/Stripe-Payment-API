import time
import names
import pandas as pd

customers = pd.read_csv("Brazilian_E-Commerce_Dataset\olist_customers_dataset.csv")

# this task takes about 15 minutes
print("assigning names to customers...")
start = time.time()
customers['customer_name'] = ""
for index, row in customers.iterrows():
    customers['customer_name'][index] = names.get_full_name()
end = time.time()
print("task finished in " + str(round(end - start, 2)) + " seconds")

## task finished in 10.47 seconds (1000 records)
## task finished in ??.?? seconds (all records)

customers.to_csv("olist_customers_dataset.csv", index=False)
