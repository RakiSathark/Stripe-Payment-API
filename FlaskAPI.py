from Transactions import *

from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

"""
CUSTOMERS:

Endpoints for customers information

Send data within customer dataframe to front-end
"""
@app.route('/customer', methods=['GET'])
def returnAllCustomers():
	return jsonify({'customers' : customer_lst})

"""
LOCATIONS:

Endpoints for location information

Send data within locations dataframe to front-end
"""
@app.route('/location', methods=['GET'])
def returnAllLocations():
	return jsonify({'locations' : location_lst})

"""
ORDERS:

Endpoints for order information

Send data within orders dataframe to front-end
"""
@app.route('/order', methods=['GET'])
def returnAllOrders():
	return jsonify({'orders' : order_lst})

"""
ITEMS:

Endpoints for item information

Send data within items dataframe to front-end
"""
@app.route('/item', methods=['GET'])
def returnAllItems():
	return jsonify({'items' : item_lst})

"""
PAYMENTS:

Endpoints for payment information

Send data within payemnts dataframe to front-end
"""
@app.route('/payment', methods=['GET'])
def returnAllPayments():
	return jsonify({'payments' : payment_lst})

"""
REVIEWS:

Endpoints for review information

Send data within reviews dataframe to front-end
"""
@app.route('/review', methods=['GET'])
def returnAllReviews():
	return jsonify({'reviews' : review_lst})

"""
PRODUCTS:

Endpoints for product information

Send data within products dataframe to front-end
"""
@app.route('/product', methods=['GET'])
def returnAllProducts():
	return jsonify({'products' : product_lst})

"""
SELLERS:

Endpoints for sellers information

Send data within sellers dataframe to front-end
"""
@app.route('/seller', methods=['GET'])
def returnAllSellers():
	return jsonify({'sellers' : seller_lst})

"""
NAMES:

Endpoints for names translation information

Send data within names dataframe to front-end
"""
@app.route('/name', methods=['GET'])
def returnAllNames():
	return jsonify({'names' : name_lst})


if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode