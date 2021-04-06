import flask
from flask import Flask, render_template, redirect, url_for
from . import app       # . is webapp/

from . import forms


# Create a controller using flask.Flask class
# app = flask.Flask(__name__)     # __name__ is the name of the file

@app.route("/")
def home():
    return "Hello world !"

@app.route("/cities")
def cities():
    return flask.render_template("cities.html", name=name)

@app.route("/add_city", methods=["GET","POST"])
def add_city():
    form = forms.AddCity()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            name = form.city_name.data
            country = form.city_country.data
            population = form.city_population.data
            area = form.city_area.data
            return flask.render_template("cities.html", name=name, country=country, population=population, area=area )
            print(f'{name}')
        
    return flask.render_template("add_city.html", form=form)







# Run the application server
# app.run(port=5001, debug=True)

