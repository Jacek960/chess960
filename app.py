from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from positions import allpositions
from random import randint
from flask_fontawesome import FontAwesome
from datetime import date
from flask_paginate import Pagination, get_page_args

chess_positions = allpositions

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


def get_chess_position(offset=0, per_page=10):
    return chess_positions[offset: offset + per_page]

@app.route('/all-positions')
def all_positions():

    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(chess_positions)
    pagination_chess = get_chess_position(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('all_positions.html',
                           all_chess_positonts=pagination_chess,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route('/position/<int:pageID>')
def position_number(pageID):
    position = allpositions[pageID]
    position_len = len(allpositions)-1
    return render_template('position_number.html',title='By ID', position=position,position_len=position_len)

if __name__ == '__main__':
    app.run()