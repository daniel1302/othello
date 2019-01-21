#!/usr/bin/env bash


# http://flask.pocoo.org/docs/1.0/tutorial/factory/
python3 -m venv venv
pip install Flask
. venv/bin/activate

# Run the application
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
