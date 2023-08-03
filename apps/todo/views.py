from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.todo.serializer import BoardSerializer, BoardDetailSerializer, TaskSerializer, SubtaskSerializer
from apps.todo.models import Board, Task, Subtask


class BoardAPIView(APIView):

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BoardCreateAPIView(APIView):
    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
    def get(self, request, pk):
        board = Board.objects.get(id=pk)
        serializer = BoardDetailSerializer(board)
        print(serializer.data['board_column'])
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        board = Board.objects.get(id=pk)
        serializer = BoardDetailSerializer(instance=board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            board = Board.objects.get(id=pk)
            board.delete()
            return Response({"message": "Board deleted successfully."})
        except Board.DoesNotExist:
            return Response({"error": "Board does not exist."}, status=status.HTTP_404_NOT_FOUND)


class TasksAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TasksCreateAPIView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSubtaskView(APIView):
    def delete(self, request, pk):
        subtask = Subtask.objects.get(id=pk)
        subtask.delete()
        return Response({"message": "Subtask deleted successfully. "}, status=status.HTTP_204_NO_CONTENT)


class MarkSubtaskDone(APIView):
    def put(self, request, pk):
        try:
            subtask = Subtask.objects.get(id=pk, is_completed=False)
            subtask.is_completed = True
            subtask.save()
            serializer = SubtaskSerializer(subtask)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subtask.DoesNotExist:
            return Response({"error": "Subtask does not exist."}, status=status.HTTP_404_NOT_FOUND)


class MarkSubtaskNotDone(APIView):
    def put(self, request, pk):
        try:
            subtask = Subtask.objects.get(id=pk, is_completed=True)
            subtask.is_completed = False
            subtask.save()
            serializer = SubtaskSerializer(subtask)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subtask.DoesNotExist:
            return Response({"error": "Subtask does not exist."}, status=status.HTTP_404_NOT_FOUND)

