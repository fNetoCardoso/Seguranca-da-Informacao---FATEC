from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:asterisk@127.0.0.1:3306/users"

db = SQLAlchemy(app)
app.app_context().push()