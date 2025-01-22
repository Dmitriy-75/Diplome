"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path
from study.views import UserViewSet, TaskViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/user_class', UserViewSet.as_view({'get': 'get'}), name='all_user'),
    path('api/user_class', UserViewSet.as_view({'get': 'post'}), name='post_user'),
    path('api/user_class/<int:user_id>', UserViewSet.as_view({'get': 'retrive'}), name='retrive_user'),
    path('api/user_class/<int:user_id>', UserViewSet.as_view({'get': 'delete'}), name='delete_user'),
    path('api/user_class/<int:user_id>', UserViewSet.as_view({'get': 'put'}), name='put_user'),

    path('api/task_class', TaskViewSet.as_view({'get': 'get'}), name='all_task'),
    path('api/task_class/<int:task_id>', TaskViewSet.as_view({'get': 'retrive'}), name='retrive_task'),
    path('api/task_class', TaskViewSet.as_view({'get': 'post'}), name='post_task'),
    path('api/task_class/<int:task_id>', TaskViewSet.as_view({'get': 'put'}), name='put_task'),
    path('api/task_class/<int:task_id>', TaskViewSet.as_view({'get': 'delete'}), name='delete_task'),
]
