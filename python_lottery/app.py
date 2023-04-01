# let the computer allow the user to access the
# build a web structure
# pip install flask

from flask import Flask, render_template
from random import randint
# application of web is created
app = Flask(__name__)

personality = ['Architect', 'Logician', 'Commander', 'Debater', 'Advocate', 'Mediator', 'Protagonist', 'Campaigner',
               'Logistician', 'Defender', 'Executive', 'Consul', 'Virtuoso', 'Adventurer', 'Entrepreneur', 'Entertainer']


@app.route('/index')
# def a index
def index():
    return render_template('index.html', personality=personality)


@app.route('/lottery')
def lottery():
    num = randint(0, len(personality)-1)
    return render_template('index.html', personality=personality, p=personality[num])


# start run the application
app.run(debug=True)
