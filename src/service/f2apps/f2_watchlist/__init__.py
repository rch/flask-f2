from flask import Blueprint, render_template

f2 = Blueprint('f2_watchlist', __name__, static_folder='static', template_folder='templates')

@f2.route('/', methods=['GET'])
def index():
	return 'Watchlist'

@f2.route('/appclass.js', methods=['GET'])
def appclass():
	return render_template('f2/app/watchlist/appclass.js', )

@f2.route('/manifest.js', methods=['GET'])
def manifest():
	return render_template('f2/app/watchlist/manifest.js', )
