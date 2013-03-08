{
	"js": [
		{
			"appId": "com_openf2_examples_javascript_helloworld",
			"manifestUrl": "{{ url_for('f2_helloworld.manifest') }}",
			"name": "Hello World (JavaScript)"
		},
		{
			"appId": "com_openf2_examples_javascript_chart",
			"height": 300,
			"minGridSize": 6,
			"isSecure": false,
			"manifestUrl": "{{ url_for('f2_chart.manifest') }}",
			"name": "Price Movement Chart"
		},
		{
			"appId": "com_openf2_examples_javascript_quote",
			"manifestUrl": "{{ url_for('f2_quote.manifest') }}",
			"name": "Quote",
			"views": ["home", "settings", "about"],
			"minGridSize": 3
		},
		{
			"appId": "com_openf2_examples_javascript_watchlist",
			"manifestUrl": "{{ url_for('f2_watchlist.manifest') }}",
			"name": "Watchlist",
			"views": ["home", "settings"],
			"minGridSize": 3
		},
		{
			"appId": "com_openf2_examples_javascript_cds",
			"manifestUrl": "{{ url_for('f2_cds.manifest') }}",
			"name": "CDS Sovereign Big Movers",
			"views": ["home", "about"],
			"minGridSize": 4
		}
	],
	"python":[
		{
			"appId": "com_openf2_dwywd_retailinterest",
			"height": 300,
			"minGridSize": 6,
			"isSecure": false,
			"manifestUrl": "{{ url_for('f2_retailinterest.manifest') }}",
			"name": "Retail Interest",
			"views": ["home", "about"]
		},
		{
			"appId": "com_openf2_examples_php_f2wits",
			"height": 200,
			"minGridSize": 4,
			"manifestUrl": "{{ url_for('f2_wits.manifest') }}",
			"name": "F2wits",
			"views": ["home","about"]
		},
		{
			"appId": "com_openf2_examples_php_marketnews",
			"manifestUrl": "{{ url_for('f2_marketnews.manifest') }}",
			"name": "Market News",
			"views": ["home", "settings"],
			"minGridSize": 4
		},
		{
			"appId": "com_openf2_examples_php_news",
			"manifestUrl": "{{ url_for('f2_news.manifest') }}",
			"name": "Stocks News",
			"views": ["home", "settings"],
			"minGridSize": 4
		}     
	]
}