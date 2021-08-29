from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.api.serializers import TaskSerializer
from todo.models import Task


@api_view(['GET'])
def apiOverview(request):
    app_urls = {
        'todo': {
            'list': '/todo/api/list/',
            'detail': '/todo/api/details/',
            'create': '/todo/api/create/',
            'update': '/todo/api/update/',
            'delete': '/todo/api/delete/',
            },
        }
    return Response(app_urls)

@api_view(['GET'])
def tasksList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response()
