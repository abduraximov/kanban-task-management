from django.contrib import admin
from apps.todo.models import Board, BoardColumn, Task, Subtask


class TaskAdmin(admin.ModelAdmin):
    fields = ("title", "description", "status")


admin.site.register(Board)
admin.site.register(BoardColumn)
admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask)

