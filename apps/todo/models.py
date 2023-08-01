from django.db import models
from apps.common.models import BaseModel


class Board(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class BoardColumn(BaseModel):
    name = models.CharField(max_length=64)
    board = models.ForeignKey("todo.Board",
                              on_delete=models.CASCADE,
                              related_name="board_column",
                              verbose_name="board"
                              )

    def __str__(self):
        return self.name


class Task(BaseModel):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    status = models.ForeignKey("todo.BoardColumn",
                               on_delete=models.CASCADE,
                               related_name="task",
                               verbose_name="status"
                               )

    def __str__(self):
        return self.title


class Subtask(BaseModel):
    name = models.CharField(max_length=64)
    is_completed = models.BooleanField(default=False)
    task = models.ForeignKey("todo.Task",
                             on_delete=models.CASCADE,
                             related_name="subtask",
                             verbose_name="task"
                             )

    def __str__(self):
        return self.name

