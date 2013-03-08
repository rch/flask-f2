from flask import Blueprint, current_app, render_template

f2 = Blueprint('f2', __name__, static_folder='static', template_folder='templates')

@f2.route('/', methods=['GET','POST','PUT','DELETE'])
def index():
    return render_template('f2/index.html', )

@f2.route('/js/examples.js', methods=['GET'])
def examples_js():
    return render_template('f2/js/examples.js', )

@f2.route('/js/sampleApps.js', methods=['GET'])
def sample_apps_js():
    return render_template('f2/js/sampleApps.js', )
