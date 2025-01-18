from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','content','user_id',)
    list_filter = ('title','user_id',)
    search_fields = ('title',)

@admin.register(User)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname', 'email','age','job',)
    list_filter = ('age',)
    search_fields = ('firstname',)