from django.urls import path, include
from .views import TodoList, TodoDetail
from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register('todo', views.TodoViewSet, basename='todo')
# urlpatterns = [

# ]
# urlpatterns += router.urls

urlpatterns = [
    path('todo/', TodoList.as_view(), name='todo-list'),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]
