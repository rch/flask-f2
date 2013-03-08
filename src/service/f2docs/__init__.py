from flask import Blueprint, current_app, render_template

f2 = Blueprint('f2_docs', __name__, static_folder='static', template_folder='templates')

@f2.route('/', methods=['GET'])
def index():
	return render_template('f2/docs/index.html', )

@f2.route('/sdk', methods=['GET'])
def sdk_index():
	return render_template('f2/docs/sdk/index.html', )
