from django.shortcuts import render
from .models import Project,Task
from .serializer import ProjectSerializer,TaskSerializer
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    
    
class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id =self.request.query_params.get('project_id',None)
        task_id=self.request.query_params.get('task_id',None)
        developer=self.request.query_params.get('developer',None)
        print(project_id,task_id)
        if project_id is not None:
            print("project true")
            queryset=Task.objects.filter(project_title_id=project_id)
        if project_id and task_id is not None:
            print("task true")
            queryset=Task.objects.filter(project_title_id=project_id).filter(id=task_id)
        if developer is not None:
            print("username true")
            queryset=Task.objects.filter(developer=developer)
        # print(queryset)
        return queryset

    
class TaskUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id =self.request.query_params.get('project_id',None)
        task_id=self.request.query_params.get('task_id',None)
        print(project_id,task_id)
        if project_id and task_id is not None:
            print("task true")
            queryset=Task.objects.filter(project_title_id=project_id).filter(id=task_id)
        # print(queryset)
        return queryset


# class ActivityViewSet(viewsets.ModelViewSet):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     # permission_classes = [
#     #     IsAuthenticated,
#     # ]

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def StatisticApiView(request):
#     if request.method=='GET':
#         project = Project.objects.all();
#         task=Task.objects.all();
#         project_object=[];
#         for(i=0;i<project.len)
#         print(project,task)
#         serializer = ProjectSerializer(project, many=True)
#         return Response(serializer.data)


# class StatisticApiView(APIView):

#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAdminUser]


#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [permission() for permission in (AllowAny,)]
#         return super(StatisticApiView, self).get_permissions()

#     def get(self, request, format=None):
#         snippets = Project.objects.all();
#         print(snippets);
#         serializer = ProjectSerializer(snippets, many=True)
#         return Response(serializer.data)

class StatisticModelView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset


