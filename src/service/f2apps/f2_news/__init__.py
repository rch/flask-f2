from flask import Blueprint, current_app, request, render_template
import requests

f2 = Blueprint('f2_news', __name__, static_folder='static', template_folder='templates')

@f2.route('/', methods=['GET'])
def index():
	return 'News'

@f2.route('/appclass.js', methods=['GET'])
def appclass():
	return render_template('f2/app/news/appclass.js', )

@f2.route('/manifest.js', methods=['GET'])
def manifest():
	return render_template('f2/app/news/manifest.js', )
