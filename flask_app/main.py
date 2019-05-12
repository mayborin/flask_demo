import json
import time
import hashlib
from flask import Flask, jsonify, abort, request
from config import DevConfig
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache

app = Flask(__name__)
cache = Cache()
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
cache.init_app(app)

class HashedMessage(db.Model):
    __tablename__ = 'hashedmessage'

    hashedvalue = db.Column(db.String(64), primary_key=True)
    message = db.Column(db.String(50000))

    def __init__(self, hashedvalue, message):
        self.hashedvalue = hashedvalue
        self.message = message
    def __repr__(self):
        return "<'{}: {}'>".format(self.hashedvalue, self.message)

@app.route('/messages',
    methods=['POST', 'GET']
)
@cache.cached(timeout=600)
def get_hash():
    message = request.values['message'] or request.get_json(force=True)['message']
    if message is None:
        return '{"err_msg": "Please provide a message"}', 404
    else:
        hexdigest = str(hashlib.sha256(message).hexdigest())
        message_exist = HashedMessage.query.filter_by(hashedvalue=hexdigest).all()
        if not message_exist:
            hashedmessage_record = HashedMessage(hexdigest, message)
            db.session.add(hashedmessage_record)
            db.session.commit()
    return "{{'digest': '{}'}}".format(hexdigest)


@app.route('/messages/<string:hashedmessage>')
@cache.cached(timeout=600)
def get_message(hashedmessage):

    if len(hashedmessage)!=64:
        return '{"err_msg": "Message not found"}', 404
    else:
        message_exist = HashedMessage.query.filter_by(hashedvalue=hashedmessage).all()
        if message_exist:
            return jsonify(message=message_exist[0].message)
        else:
            return '{"err_msg": "Message not found"}', 404


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


if __name__ == '__main__':
    app.run()

