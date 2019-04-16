import time
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

DBUSER = 'postgres'
DBPASS = 'password123'
DBHOST = 'db'
DBPORT = '5432'
DBNAME = 'testdb'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=DBUSER,
        passwd=DBPASS,
        host=DBHOST,
        port=DBPORT,
        db=DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'password123'

db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column('student_id', db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  eid = db.Column(db.String(50))
  major = db.Column(db.String(50))

  def __init__(self, name, eid, major):
    self.name = name
    self.eid = eid
    self.major = major

def insert_students():
  db.create_all()
  student1 = Student('Madalyn', 'mm123', 'MIS')
  db.session.add(student1)
  # db.session.rollback()
  db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def home():
    return (Student.query.first().name)

if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    insert_students()
    app.run(debug=True, host='0.0.0.0')
