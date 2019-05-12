from flask.ext.script import Manager, Server
from main import app, db, HashedMessage

manager = Manager(app)
manager.add_command("server", Server(host='0.0.0.0', port=5000))

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, HashedMessage=HashedMessage)

@manager.command
def setup_db():
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    manager.run()

