import markdown
from flask import Flask
from flask import Flask, render_template, url_for, send_from_directory

import markdown.extensions.fenced_code

app = Flask(__name__)

@app.route('/')
def index(username=None):
    return render_template('index.html')

@app.route("/lesson1/lesson")
def lesson1_lesson():
    readme_file = open("./lesson1/in-this-chapter.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )

    return md_template_string

@app.route("/lesson1/exercises")
def lesson1():
    readme_file = open("./lesson1/exercises.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )

    return md_template_string


if __name__ == "__main__":
    app.run()