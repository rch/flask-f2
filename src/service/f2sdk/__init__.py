from flask import Blueprint

f2 = Blueprint('f2_sdk', __name__, static_folder='static')

@f2.route('/', methods=['GET'])
def index():
	return 'SDK'
