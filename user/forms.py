import re
from flask_wtf import Form
from wtforms import TextAreaField, TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length. EqualTo

from app.models import User

class LoginForm(Form):
	email = TextField('email', validators=[DataRequired(), Email()])
	password = PasswordField('password', validators=[DataRequired()])

class RegistrationForm(Form):
	first_name = TextField(
		'first_name', 
		validators=[DataRequired(), Length(min=2, max=15)])
	last_name = TextField(
		'last_name', 
		validators=[DataRequired(), Length(min=2, max=25)])
	major = TextField(
		'major', 
		validators=[DataRequired(), Length(min=6, max=40)])
	interests = TextField(
		'interests', 
		validators=[DataRequired(), Length(min=15, max=140)])
	phone = TextField(
		'phone', 
		validators=[DataRequired(), Length(min=10, max=10,
					message="Include digits only (ex: 123456000")])
	email = TextField(
		'email', 
		validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
	password = PasswordField(
		'password', 
		validators=[DataRequired(), Length(min=6, max=30)])
	confirm = PasswordField(
		'Repear password', 
		validators=[DataRequired(), EqualTo('password',
					message='Passwords must match')])

	def validate(self):
		initial_validation = super(Registration, self).validate()
		if not initial_validation:
			return False
		user = User.query.filter_by(email=self.email.data).first()
		if user:
			self.email.errors.append("Email already registered.")
			return False
		user = User.query.filter_by(phone=self.phone.data).first()
		if user:
			self.phone.errors.append("Phone number already registered.")
			return False
		return True


class ChangePasswordForm(Form):
	password = PasswordField(
		'password', 
		validators=[DataRequired(), Length(min=6, max=30)])
	confirm = PasswordField(
		'Repear password', 
		validators=[DataRequired(), EqualTo('password',
					message='Passwords must match')])

class EditProfileForm(Form):
	major = TextAreaField('major', validators=[Length(min=6, max=40)])
	interests = TextAreaField('interests', validators=[Length(min=6, max=40)])
	about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
	instagram = TextAreaField('instagram', validators=[Length(min=0, max=30)])
	twitter = TextAreaField('twitter', validators=[Length(min=0, max=15)])


