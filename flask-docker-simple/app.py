import time
from flask import Flask, render_template

app = Flask(__name__)

class Student():
  def __init__(self, name, eid, major):
    self.name = name
    self.eid = eid
    self.major = major

@app.route('/')
def home():
  student1 = Student('Madalyn', 'mm123', 'MIS')
  student2 = Student('Shaana', 'it000', 'Economics')
  students = [student1, student2]
  return render_template('Students.html', students = students)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
