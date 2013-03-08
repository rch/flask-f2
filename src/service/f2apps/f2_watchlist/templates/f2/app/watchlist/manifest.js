F2_jsonpCallback_com_openf2_examples_javascript_watchlist({
	"scripts":[
		"{{ url_for('f2_watchlist.static', filename='f2/app/watchlist/jquery.cookie.js') }}",
		"{{ url_for('f2_watchlist.static', filename='f2/app/watchlist/moment.1.7.0.min.js') }}",
		"{{ url_for('f2_watchlist.appclass') }}"
	],
	"styles":[
		"{{ url_for('f2_watchlist.static', filename='f2/app/watchlist/watchlist.css') }}"
	],
	"apps":[
		{
			"html":[
				'<div>',
					'<div class="f2-app-view" data-f2-view="home">',
						'<div class="watchlist"></div>',
						'<div class="input-append">',
							'<input type="text" name="lookup" class="spanx input-small">',
							'<button type="button" class="btn add">Add to List</button>',
						'</div>',
						'<p>',
							'<small>Market data delayed at least 15 minutes. <a href="http://developer.yahoo.com/yql/" target="_blank">By Yahoo!</a></small>',
						'</p>',
					'</div>',
					'<form class="f2-app-view hide" data-f2-view="settings">',
						'<h3>Settings</h3>',
						'<span class="help-block">This App can listen for symbols from nearby Apps which allows <em>other apps</em> to add symbols to this watchlist.</span>',
						'<span class="help-block">Allow Symbols from Nearby Apps</span>',
						'<label class="radio">',
							'<input type="checkbox" name="allowExternalAdd" checked="checked"> Yes',
						'</label>',
						'<div class="form-actions">',
							'<button type="button" class="btn btn-custom1 save">Save</button> ',
							'<button type="button" class="btn btn-custom2 cancel f2-app-view-trigger" data-f2-view="home">Cancel</button>',
						'</div>',
					'</form>',
					'<div class="f2-app-view hide" data-f2-view="about">',
						'<h3>About</h3>',
						'<p>Quick Quote App v0.12.3</p>',
						'<p><a href="#" class="f2-app-view-trigger" data-f2-view="home">&laquo; Back</a>',
					'</div>',
				'</div>'
			].join("")
		}
	]
})