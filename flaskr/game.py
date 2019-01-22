import functools

from flask import (
            Blueprint, flash, g, redirect, render_template, request, session, url_for
            )
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route('/index', methods=('GET'))  
def index():


    return render_template('game/index.html');


@bp.route('/move', methods=('POST'))
def move():

    return redirect(url_for('game.index'))
