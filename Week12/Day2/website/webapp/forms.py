import flask_wtf
import wtforms 
from wtforms import validators as vld

# Form class --> flask_wtf.FlaskForm
# Form fields --> wtforms.SomethingField

# each form is a class inheriting from flask_wtf.FlaskForm
# every class attribute is a field in the form

class AddCity(flask_wtf.FlaskForm):

    city_name = wtforms.StringField("City's Name: ", validators=[vld.Length(min=4, max=25, message="Please enter a name between 4 and 25 characters."),
    vld.DataRequired(message="Please Enter The City's Name")])
    
    city_country = wtforms.StringField("City's Country: ", validators=[vld.DataRequired(message="Please Enter the City's Country.'")])
    city_population = wtforms.IntegerField("City's Population: ", validators=[vld.DataRequired(message="Please Enter the City's Population.")])
    city_area = wtforms.IntegerField("City's Area: ")


    submit = wtforms.SubmitField("Submit")


