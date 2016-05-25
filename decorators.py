from functools import wraps
from flaskimport flash, redirect, url_for
from flask.ext.login import current_user

# confirms user for app service
def is_confirmed(func):
	@wraps(func)
	def decorated_function(*args, **kwargs):
		if current_user.confirmed is False:
			flash('Please confirm your account!', 'warning')
			return redirect(url_for('user.confirmed'))
		return func(*args, **kwargs)
	return decorated_function