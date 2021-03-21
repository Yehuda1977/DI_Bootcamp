from products_data import retrieve_all_products, retrieve_requested_product

import flask
from flask import Flask, render_template, redirect, url_for


# Create a controller using flask.Flask class
app = flask.Flask(__name__)     # __name__ is the name of the file

all_products = retrieve_all_products()
cart_item = []

def total():
    total_price = 0
    for item in cart_item:
        total_price += item['Price']
    return total_price


# Create one route: a function that is assigned to a URL
# 127.0.0.1:5000/ <--> route "/"
# 127.0.0.1:5000/home <--> route "/home"
@app.route("/")
def homepage():
    return render_template('welcome.html')

@app.route("/products")
def products():  
    return render_template('products.html', all_products=all_products)

@app.route("/products/<product_id>")
def one_product(product_id):
    product = retrieve_requested_product(product_id, all_products)
    return render_template('product.html', product=product)

@app.route("/cart")
def cart():
    total_price = total()
    return render_template('cart.html', cart_item=cart_item, total=total_price)

@app.route("/add_product_to_cart/<product_id>")
def add_to_cart(product_id):
    product = retrieve_requested_product(product_id, all_products)
    cart_item.append(product)
    return redirect(url_for('cart'))

@app.route("/delete_product_from_cart/<product_id>")
def delete_from_cart(product_id):
    product = retrieve_requested_product(product_id, all_products)
    cart_item.remove(product)
    return redirect(url_for('cart'))


# Run the application server
app.run(port=5001, debug=True)


