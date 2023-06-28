from django.urls import path,include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'task', views.TaskViewSet,basename="task-list")
# router.register(r'statistic', views.StatisticModelView,basename="statistic")
# router.register(r'activity', views.ActivityViewSet)

urlpatterns=[
   path('', include(router.urls)),
   path('update_task/',views.TaskUpdateApiView.as_view(),name='update-task'),
   # path('statistic2/',views.StatisticApiView,name="statistics-api")
   # path('statistic2/',views.StatisticApiView.as_view(),name="statistics-api")
   # path('',views.ProjectListCreateView.as_view(),name='project-list'),
   # path('task/',views.TaskListCreateView.as_view(),name='task-list')

]