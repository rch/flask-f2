F2_jsonpCallback_com_openf2_examples_javascript_chart({
	"scripts":[
		"http://code.highcharts.com/highcharts.js",
		"{{ url_for('f2_chart.appclass') }}"
	],   
	"styles":[
		"{{ url_for('f2_chart.static', filename='f2/app/chart/app.css') }}"
	],   
	"apps":[{
		"html":[
			'<div class="f2-app-view">',
				'<div id="f2-1year-chart-container">',
					'<div id="f2-1year-chart"></div>',
				'</div>',
			'</div>'
		].join("")
	}]
})