from app import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstname", "lastname","email","age","job")


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content", "priority", "completed", "user_id", "slug")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)