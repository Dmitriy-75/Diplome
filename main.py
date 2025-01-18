from app.resources import UserListResource, UserResource, TaskListResource, TaskResource
from app import api
from app import app
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(TaskListResource, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')


if __name__ == '__main__':
    app.run(debug=True)


