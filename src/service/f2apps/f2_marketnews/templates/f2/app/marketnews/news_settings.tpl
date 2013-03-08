<form class="f2-app-view hide" data-f2-view="settings">
	<label class="checkbox" name="autoRefresh">
		<input type="checkbox" name="autoRefresh"> 30-Second Auto-Refresh
	</label>
	<span class="help-block">News Provider:</span>
	{% for key, value in providers %}
	<label class="radio">
		<input type="radio" name="provider" value="{{ key }}" {% if key == provider.id %}checked {% endif %}>
		{{ value.display }}
	</label>
	{% endfor %}
	<div class="form-actions">
		<button type="button" class="btn btn-primary save">Save</button>
		<button type="button" class="btn cancel">Cancel</button>
	</div>
</form>
