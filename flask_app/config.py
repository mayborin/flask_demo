class Config(object):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    CACHE_TYPE = 'simple'

class ProdConfig(Config):
    pass

