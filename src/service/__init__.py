from flask import Flask, Blueprint, request, session, render_template, url_for

app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key = 'not2398fjk;;aaa.qweqw.key2129'

from f2apps.f2_helloworld import f2 as f2_helloworld
app.register_blueprint(f2_helloworld, url_prefix='/f2/app/helloworld')

from f2apps.f2_chart import f2 as f2_chart
app.register_blueprint(f2_chart, url_prefix='/f2/app/chart')

from f2apps.f2_cds import f2 as f2_cds
app.register_blueprint(f2_cds, url_prefix='/f2/app/cds')

from f2apps.f2_quote import f2 as f2_quote
app.register_blueprint(f2_quote, url_prefix='/f2/app/quote')

from f2apps.f2_watchlist import f2 as f2_watchlist
app.register_blueprint(f2_watchlist, url_prefix='/f2/app/watchlist')

from f2apps.f2_wits import f2 as f2_wits
app.register_blueprint(f2_wits, url_prefix='/f2/app/wits')

from f2apps.f2_marketnews import f2 as f2_marketnews
app.register_blueprint(f2_marketnews, url_prefix='/f2/app/marketnews')

from f2apps.f2_news import f2 as f2_news
app.register_blueprint(f2_news, url_prefix='/f2/app/news')

from f2apps.f2_retailinterest import f2 as f2_retailinterest
app.register_blueprint(f2_retailinterest, url_prefix='/f2/app/retailinterest')

from f2container import f2
app.register_blueprint(f2, url_prefix='/f2')

from f2docs import f2 as f2_docs
app.register_blueprint(f2_docs, url_prefix='/f2/docs')

from f2sdk import f2 as f2_sdk
app.register_blueprint(f2_sdk, url_prefix='/f2/sdk')

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/')
def view_index():
    return render_template('index.html', )
    
if __name__ == '__main__':
    app.run()
