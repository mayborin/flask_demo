from flask.ext.script import Manager, Server
from main import app, db, HashedMessage

manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
	return dict(app=app, db=db, HashedMessage=HashedMessage)

if __name__ == "__main__":
	manager.run()

