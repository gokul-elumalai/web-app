import requests

from program import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/100Days')
def p100Days():
    return render_template('100Days.html')


@app.route('/chuck')
def chuck():
    joke = get_chuck_joke()
    return render_template('chuck.html', joke=joke)


@app.route('/advice')
def advice():
    sentence = get_advice()
    return render_template('advice.html', advice=sentence)


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']


def get_advice():
    r = requests.get('https://api.adviceslip.com/advice')
    data = r.json()
    return data['slip']['advice']
