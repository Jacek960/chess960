from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from positions import allpositions
from random import randint
from flask_fontawesome import FontAwesome
from datetime import date


app = Flask(__name__)
Bootstrap(app)
fa = FontAwesome(app)

@app.context_processor
def inject_today_date():
    return {'year': date.today().year}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/random')
def random():
    positions = allpositions
    random = randint(0,len(allpositions)-1)
    return render_template('random.html', random=random,positions=positions)


@app.route('/all-positions')
def all_positions():
    positions = allpositions
    return render_template('all_positions.html', positions=positions)

@app.route('/position/<int:pageID>')
def position_number(pageID):
    position = allpositions[pageID]
    position_len = len(allpositions)-1
    return render_template('position_number.html',title='By ID', position=position,position_len=position_len)

if __name__ == '__main__':
    app.run()