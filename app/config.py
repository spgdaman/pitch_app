class Config:
    SECRET_KEY = 'sIM0n'

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    pass