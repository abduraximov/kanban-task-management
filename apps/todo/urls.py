from django.urls import path
from apps.todo.views import (BoardAPIView, BoardDetail,
                             BoardCreateAPIView, TaskDetailAPIView,
                             TasksAPIView, TasksCreateAPIView,
                             )

urlpatterns = [
    path("boards/", BoardAPIView.as_view(), name="boards"),
    path("boards/create/", BoardCreateAPIView.as_view(), name="boards"),
    path("boards/<int:pk>/", BoardDetail.as_view(), name="detail"),
    path("boards/tasks/", TasksAPIView.as_view(), name="tasks"),
    path("boards/tasks/create/", TasksCreateAPIView.as_view(), name="task_create"),
    path("boards/tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task_detail"),
]
