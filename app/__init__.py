from flask import Flask

app = Flask(__name__)

bootstrap = Bootstrap(app)

from app import views