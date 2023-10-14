from flask import Flask
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

#engine = create_engine("mysql+pymysql://root:senha123@localhost:5007/users", echo=True)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:senha123@localhost:3306/users"

db.init_app(app)