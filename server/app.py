# https://gist.github.com/miguelgrinberg/5614326
from flask import Flask, request, url_for
from flask_cors import CORS
from ResponseHandler import ResponseHandler

# configuration
DEBUG = True
ROOT_PATH = "/sensei/api/v1"

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# create dictionary list
students = [
    {
        'id': 1,
        'firstName': 'Asher',
        'lastName': 'Stark', 
        'class': 'Kids'
    },
    {
        'id': 2,
        'firstName': 'Austin',
        'lastName': 'Stark', 
        'class': 'Kids'
    },
    {
        'id': 3,
        'firstName': 'Harrison',
        'lastName': 'Street', 
        'class': 'LilNinjas'
    },
    {
        'id': 4,
        'firstName': 'Jeremy',
        'lastName': 'Friedman', 
        'class': 'Adults'
    },
    {
        'id': 5,
        'firstName': 'Riley',
        'lastName': 'Studabaker', 
        'class': 'Kids'
    },
]

# Routes
# Students
####################################################
@app.route(f'{ROOT_PATH}/students', methods=['GET'])
def get_students():
    return ResponseHandler(students).toJSON()

@app.route(f'{ROOT_PATH}/students/<int:task_id>', methods=['GET'])
def get_student(task_id):
    student = list(filter(lambda t: t['id'] == task_id, students))
    if len(student) == 0:
        return ResponseHandler(errorMessage = "Record not found").toJSON()
    return ResponseHandler(payload=student[0]).toJSON()

@app.route(f'{ROOT_PATH}/students', methods=['POST'])
def save_student():
    if not request.json:
        return ResponseHandler(errorMessage = "Title cannot be empty").toJSON()
    if not request.json or not 'title' in request.json or not request.json['title']:
        return ResponseHandler(errorMessage = "Title cannot be empty").toJSON()
    student = {
        'id': students[-1]['id'] + 1,
        'firstName': request.json['firstName'],
        'lastName': request.json('lastName'),
        'class': request.json('class'),
        # 'class': request.json.get('class', False)
    }
    students.append(student)
    return ResponseHandler(student).toJSON()
####################################################

if __name__ == '__main__':
    app.run()
