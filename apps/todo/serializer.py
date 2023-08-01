from rest_framework import serializers
from apps.todo.models import Board, BoardColumn, Task, Subtask


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = (
            "id",
            "name",
        )

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short. ")
        return value


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = (
            "id",
            "name",
            "is_completed",
        )


class TaskSerializer(serializers.ModelSerializer):
    subtask = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "subtask",
        )


class BoardColumnSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)

    class Meta:
        model = BoardColumn
        fields = (
            "id",
            "name",
            "task",
        )


class BoardDetailSerializer(serializers.ModelSerializer):
    board_column = BoardColumnSerializer(many=True, read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Board
        fields = (
            "id",
            "name",
            "board_column",
        )

