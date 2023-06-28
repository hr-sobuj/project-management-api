from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet,basename="user-list")

urlpatterns=[
   path('user/', include(router.urls)),
   path('dev/register/', views.RegisterView.as_view(), name='auth_register'),
   # path('',views.ProjectListCreateView.as_view(),name='project-list'),
   # path('task/',views.TaskListCreateView.as_view(),name='task-list')

]