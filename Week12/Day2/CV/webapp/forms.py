import flask_wtf
import wtforms 
from wtforms import validators as vld

# Form class --> flask_wtf.FlaskForm
# Form fields --> wtforms.SomethingField

# each form is a class inheriting from flask_wtf.FlaskForm
# every class attribute is a field in the form

class Form(flask_wtf.FlaskForm):

    first_name = wtforms.StringField("First Name: ", validators=[vld.Length(min=4, max=25, message="Please enter a name between 4 and 25 characters."),
    vld.DataRequired(message="Please Enter Your First Name")])
    last_name = wtforms.StringField("Last Name: ", validators=[vld.Length(min=4, max=25, message="Please enter a name between 4 and 25 characters."),
    vld.DataRequired(message="Please Enter Your Last Name")])
    age = wtforms.IntegerField("Age: ")
    experience = wtforms.TextAreaField("Experience:")
    
    
    

    submit = wtforms.SubmitField("Submit")


