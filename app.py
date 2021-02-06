from flask import Flask, url_for, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/data')
def data():
    url = "https://randomuser.me/api/?results=12"
    data = requests.get(url).json()

    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)