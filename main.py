import json
from flask import Flask, jsonify, abort
from config import DevConfig
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	
	def __init__(self, username):
		self.username = username
	def __repr__(self):
		return "<User '{}'>".format(self.username)

@app.route('/<message>')
def home(message):
	return jsonify(res=message.lower())

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
	app.run()

