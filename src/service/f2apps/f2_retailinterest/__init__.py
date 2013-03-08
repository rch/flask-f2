from flask import Blueprint, render_template

f2_appname = 'retailinterest'

f2 = Blueprint('f2_%s' % f2_appname, __name__, static_folder='static', template_folder='templates')

@f2.route('/', methods=['GET'])
def index():
	return 'Hello World'
	
@f2.route('/appclass.js', methods=['GET'])
def appclass():
	return render_template('f2/app/%s/appclass.js' % f2_appname, )
	
@f2.route('/manifest.js', methods=['GET'])
def manifest():
	return render_template('f2/app/%s/manifest.js' % f2_appname, )
	