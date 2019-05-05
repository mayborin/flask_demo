class Config(object):
	pass

class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

class ProdConfig(Config):
	pass

