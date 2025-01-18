import flask

from app import db
from app.models import User, Task
from app.shema import users_schema, user_schema, tasks_schema, task_schema
from app import Resource
from flask import Flask, request, Response




class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        new_user = User(
            firstname=request.json['firstname'],
            lastname=request.json['lastname'],
            email=request.json['email'],
            age=request.json['age'],
            job=request.json['job']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)
    def patch(self, user_id):
        user = User.query.get_or_404(user_id)
        if 'firstname' in request.json:
            user.firstname = request.json['firstname']
        if 'lastname' in request.json:
            user.lastname = request.json['lastname']
        if 'email' in request.json:
            user.email = request.json['email']
        if 'age' in request.json:
            user.age = request.json['age']
        if 'job' in request.json:
            user.job = request.json['job']

        db.session.commit()
        return user_schema.dump(user)
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return Response ({"message": "Objects deleted successfully"}, status=201)

class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return tasks_schema.dump(tasks)

    def post(self):
        new_task = Task(
            title=request.json['title'],
            content=request.json['content'],
            priority=request.json['priority'],
            completed=request.json['completed'],
            user_id=request.json['user_id'],
            slug=request.json['slug']
        )
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task)

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return task_schema.dump(task)
    def patch(self, task_id):
        task = Task.query.get_or_404(task_id)
        if 'title' in request.json:
            task.title = request.json['title']
        if 'content' in request.json:
            task.content = request.json['content']
        if 'priority' in request.json:
            task.priority = request.json['priority']
        if 'completed' in request.json:
            task.completed = request.json['completed']
        if 'user_id' in request.json:
            task.user_id = request.json['user_id']
        db.session.commit()
        return task_schema.dump(task)
    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return  Response ({"message": "Objects deleted successfully"}, status=201)
