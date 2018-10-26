import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = 'files/'
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
CORS(app, resources={r"/*": {"origins": "*"}})
