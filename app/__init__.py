from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(DevConfig)

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)

from app import views