<div class="f2-app-view" data-f2-view="home">
	<ul class="unstyled">
		{% for item in provider %}
		<li>
			<article>
				<header>
					<a href="{{ item.link }}" target="_blank" class="newsTitle">{{ item.title }}</a>
					<time>{{ item.date }}</time>
				</header>
				<summary>
					{{ item.desc }}
				</summary>
			</article>
		</li>
		{% endfor %}
	</ul>
	<footer>Copyright &copy; 2013 {{ provider.display }}</footer>
</div>
