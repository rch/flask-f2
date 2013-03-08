from flask import Blueprint, current_app, request, render_template
import requests

f2 = Blueprint('f2_wits', __name__, static_folder='static', template_folder='templates')

@f2.route('/', methods=['GET'])
def index():
	return 'Stocktwits'

@f2.route('/appclass.js', methods=['GET'])
def appclass():
	return render_template('f2/app/wits/appclass.js', )

@f2.route('/manifest.js', methods=['GET'])
def manifest():
	return render_template('f2/app/wits/manifest.js', )

@f2.route('/streams/symbol', methods=['GET'])
def stocktwits():
	# http://stocktwits.com/developers/docs/api#streams-symbol-docs
	print request.args
	r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/%s.json' % request.args.get('symbol', 'GOOG'))
	return current_app.response_class(r.text, mimetype='application/json')
