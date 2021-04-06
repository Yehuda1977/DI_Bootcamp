import flask


app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "secretkey"



from . import routes