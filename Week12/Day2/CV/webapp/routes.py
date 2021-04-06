import flask
# from flask import Flask, render_template, redirect, url_for
from . import app       # . is webapp/

from . import forms



# Create a controller using flask.Flask class
# app = flask.Flask(__name__)     # __name__ is the name of the file

@app.route("/")
def home():
    return "Hello world !"


@app.route("/form", methods=["GET","POST"])
def form():
    form = forms.Form()

    if flask.request.method == "POST":
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            age = form.age
            experience = form.experience.data
            
            print(f'{first_name, last_name, age, experience}')
            return flask.render_template("display.html", first_name=first_name, last_name=last_name, age=age, experience=experience)
            
        
    return flask.render_template("form.html", form=form)







# Run the application server
# app.run(port=5001, debug=True)

