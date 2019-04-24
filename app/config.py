class Config:
    SECRET_KEY = 'sIM0n'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://simon:m1m1@localhost/pitch'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass

config_options = {
    'development' : DevConfig,
    'production': ProdConfig
}