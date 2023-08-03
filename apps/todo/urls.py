from django.urls import path
from apps.todo.views import (BoardAPIView, BoardDetail,
                             BoardCreateAPIView, TaskDetailAPIView,
                             TasksAPIView, TasksCreateAPIView,
                             MarkSubtaskDone, MarkSubtaskNotDone,
                             DeleteSubtaskView)

urlpatterns = [
    path("boards/", BoardAPIView.as_view(), name="boards"),
    path("boards/create/", BoardCreateAPIView.as_view(), name="boards"),
    path("boards/<int:pk>/", BoardDetail.as_view(), name="detail"),
    path("boards/tasks/", TasksAPIView.as_view(), name="tasks"),
    path("boards/tasks/create/", TasksCreateAPIView.as_view(), name="task_create"),
    path("boards/tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task_detail"),
    path("boards/tasks/subtask/delete/<int:pk>/", DeleteSubtaskView.as_view(), name="subtask_delete"),
    path("boards/tasks/sub_task_done/<int:pk>/", MarkSubtaskDone.as_view(), name="sub_task_done"),
    path("boards/tasks/sub_task_not_done/<int:pk>/", MarkSubtaskNotDone.as_view(), name="sub_task_not_done"),

]
