from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

DBUSER = 'marco'
DBPASS = 'foobarbaz'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'testdb'


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'foobarbaz'
db = SQLAlchemy(app)
'''
class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
'''
class Genre(db.Model):
	__tablename__ = 'genres'

	genre_id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(250), nullable = False)
	url = db.Column(db.String(500), nullable = False)
	description = db.Column(db.String(5000), nullable = False)

def create_genres():
  name = 'Fiction'
  id = 1
  url = 'theurl'
  description = 'about genre'

  newGenre = Genre(genre_id = id, name = name, url = url, description = description)
  db.session.add(newGenre)
  db.session.commit()


@app.route('/')
def hello_world():
  genres = db.session.query(Genre).all()
  return (genres[0])

if __name__ == '__main__':
  print("TEST TEST TEST")
  db.drop_all()
  db.create_all()
  create_genres()
  app.run(debug=True, host='0.0.0.0')
