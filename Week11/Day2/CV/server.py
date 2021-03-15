import os
from flask import Flask, render_template, url_for, send_from_directory
app = Flask(__name__)
print(__name__)

@app.route('/<username>')
def index(username=None):
    return render_template('index.html', 
    name=username, 
    img_url="https://gethelpisrael.com/dashboard/uploads/profiles/Yehuda2.jpg",
    hobbies=['Coding', 'Jogging', 'Cooking'],
    skills=['Fishing', 'Eating', 'Yoga'],
    strengths=['Muscles', 'Throwing away garbage', 'driving'],
    weaknesses=['candy', 'cake', 'naps'])

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
app.run(port=5004)