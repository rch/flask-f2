F2_jsonpCallback_com_openf2_examples_php_f2wits({
	"scripts":[
	    "{{ url_for('f2_wits.static', filename='f2/app/wits/moment.1.7.0.min.js') }}",
	    "{{ url_for('f2_wits.appclass') }}"
	],	 
	"styles":[
	    "{{ url_for('f2_wits.static', filename='f2/app/wits/watchlist.css') }}"
	],	 
	"apps":[{
			"html":[
				'<div class="f2-app-view" data-f2-view="home"></div>',
				'<div class="f2-app-view hide" data-f2-view="about"><p>App version 1.0. Designed with F2 0.12.5</p></div>'
			].join("")
	}]
})