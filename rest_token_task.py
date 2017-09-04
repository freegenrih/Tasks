#!/usr/bin/python
from uuid import uuid4

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

cache_token = []

TASKS = {
    'task1': {'task': 'task №1'},
    'task2': {'task': 'task №2'},
    'task3': {'task': 'task №3'},
}


def abort_if_task_doesnt_exist(task_id):
    if task_id not in TASKS:
        abort(404, message="Task {} doesn't exist".format(task_id))


def abort_if_token_doesnt_exist(master_token):
    if master_token not in cache_token :
        abort(401, message=" Unauthorized ")


def availability_of_a_token():
    args = parser.parse_args()
    master_token = args['master_token']
    abort_if_token_doesnt_exist(master_token)


parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('master_token')


class Home(Resource):
    def get(self):
        gen_master_token = str(uuid4())
        cache_token.append(gen_master_token)
        return {'master_token': gen_master_token}


class TaskList(Resource):
    def get(self):
        availability_of_a_token()
        return TASKS

    def post(self):
        availability_of_a_token()
        args = parser.parse_args()
        task_id = int(max(TASKS.keys()).lstrip('task')) + 1
        task_id = 'task{}'.format(str(task_id))
        TASKS[task_id] = {'task': args['task']}
        return TASKS[task_id], 201


class TaskEdit(Resource):
    def get(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        availability_of_a_token()
        return TASKS[task_id]

    def delete(self, task_id):
        abort_if_task_doesnt_exist(task_id)
        availability_of_a_token()
        del TASKS[task_id]
        return '', 204

    def put(self, task_id):
        availability_of_a_token()
        args = parser.parse_args()
        task = {'task': args['task']}
        TASKS[task_id] = task
        return task, 201


api.add_resource(Home, '/')# endpoint generate master_token
api.add_resource(TaskList, '/tasks')
api.add_resource(TaskEdit, '/tasks/<task_id>')



if __name__ == '__main__':
    app.run(debug=True)
