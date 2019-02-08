import functools
import json

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from model import game_service

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/', methods=['GET'])
def index():
    try:
        game = game_service(session['width'], session['height'], session['board'])
        board_state = json.dumps(game.get_board())
    except Exception as e:
        flash("Nieoczekiwany blad: " + str(e))
        return redirect(url_for('game.new_game'))

    return render_template('game/index.html',
        board_state = board_state,
        board_width = game.get_size()[0],
        board_height = game.get_size()[1])


@bp.route('/new', methods=['GET', 'POST'])
def new_game():
    if request.method == 'POST':
        try:
            width = int(request.form['width'])
            height = int(request.form['height'])

            game = game_service(width, height)
            session.clear()
            session['width'] = width
            session['height'] = height
            session['board'] = game.get_board()

            return redirect(url_for('game.index'))
        except ValueError:
            flash("Niepoprawne wartosci w formularzu")


    return render_template('game/new.html')


@bp.route('/move', methods=['GET'])
def move():
    try:
        x = int(request.args.get('x'))
        y = int(request.args.get('y'))

        game = game_service(session['width'], session['height'], session['board'])
        game.move(x, y)
        session['board'] = game.get_board()
    except Exception as ex:
        print(ex)
        return jsonify({
            'status': '500',
            'error': str(ex)
        }), 500

    return jsonify(game.get_board())
