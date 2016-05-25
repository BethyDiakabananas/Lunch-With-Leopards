from flask.ext.mail import Message
from app import app, mail

def send_email(recipient, subject, template):
	message = Message(
		subject,
		recipients=[recipient],
		html=template,
		sender=app.config['MAIL_DEFAULT_SENDER'])
	mail.send(msg)