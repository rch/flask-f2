F2_jsonpCallback_com_openf2_examples_javascript_helloworld({
	"scripts":[
		"{{ url_for('f2_helloworld.appclass') }}"
	],
	"styles":[

	],
	"apps":[
		{
			"html":[
				'<div>',
					'<div class="f2-app-view" data-f2-view="home">',
						'<p>Hello World!</p>',
						'<ul>',
							'<li><a href="#" class="testAlert">Alert Modal</a></li>',
							'<li><a href="#" class="testConfirm">Confirm Modal</a></li>',
						'</ul>',
					'</div>',
				'</div>'
			].join("")
		}
	]
})