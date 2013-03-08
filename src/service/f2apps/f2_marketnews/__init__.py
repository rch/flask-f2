from flask import Blueprint, current_app, request, render_template, make_response, jsonify
from lxml import etree
import requests
from providers import DefaultProvider, YahooBusinessNews


f2 = Blueprint('f2_marketnews', __name__, static_folder='static', template_folder='templates')

templateArgs = {
	'provider': DefaultProvider(),
	'providers': [('yahooBusinessNews',YahooBusinessNews())]
}

@f2.route('/', methods=['GET'])
def index():
	return 'Market News'


@f2.route('/appclass.js', methods=['GET'])
def appclass():
	return render_template('f2/app/marketnews/appclass.js', )


@f2.route('/manifest.js', methods=['GET'])
def manifest():
	templateArgs['news_items'] = render_template('f2/app/marketnews/news_items.tpl', **templateArgs).replace('\"','\\\"')
	templateArgs['news_settings'] = render_template('f2/app/marketnews/news_settings.tpl', **templateArgs).replace('\"','\\\"')
	response = make_response(
		render_template('f2/app/marketnews/manifest.js', **templateArgs))
	response.headers['Content-type'] = 'application/json'
	return response

@f2.route('/news', methods=['GET'])
def news():
	news_items = make_response(
		render_template('f2/app/marketnews/news_items.tpl', **templateArgs).replace('\"','\\\"'))
	return response