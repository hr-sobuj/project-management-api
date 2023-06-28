from rest_framework import serializers
from .models import Project,Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields="__all__"
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields="__all__"
# class ActivitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Activity
#         fields="__all__"