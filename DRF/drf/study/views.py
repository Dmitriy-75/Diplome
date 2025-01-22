from django.shortcuts import render
# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import TaskSerializer, UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """класс пользователей"""

    @staticmethod
    def post(self,request):
        """создаем пользователя"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @staticmethod
    def get(self):
        """получение всех пользователей"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @staticmethod
    def retrive(self, user_id):
        """пользователь по id"""
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=201)

    @staticmethod
    def delete(self, user_id):
        """удаление пользователя по id"""
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        user.delete()
        return Response({"status": "User deleted"}, status=201)

    @staticmethod
    def put(self, request, user_id):
        """корректировка пользователя"""
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data
            return Response(user, status=201)
        return Response(serializer.errors, status=400)


class TaskViewSet(viewsets.ModelViewSet):
    """класс задач"""

    @staticmethod
    def get(self):
        """получение всех задач"""
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @staticmethod
    def retrive(self, task_id):
        """получение задачи по id"""
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    @staticmethod
    def post(self, request):
        """post задачи"""
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @staticmethod
    def put(self, request, task_id):
        """корректировка задачи"""
        try:
            user = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.data
            return Response(task, status=201)
        return Response(serializer.errors, status=400)

    @staticmethod
    def delete(self, task_id):
        """удаление задачи по id"""
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        task.delete()
        return Response({"status": "Task deleted"}, status=201)
