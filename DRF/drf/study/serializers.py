from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):

    age = serializers.IntegerField(min_value=16, max_value=99)

    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'age', 'job']
        many = True

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'content', 'priority', 'completed', 'user_id', 'slug']
        many = True
