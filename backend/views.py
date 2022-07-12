from functools import partial
from django.shortcuts import render
from .models import Project,Task,SubTask
from .serializers import ProjectSerializer,TaskSerializer,SubTaskSerializer
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class TaskApiView(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request,pk,format=None):
        obj = self.get_object(pk)
        serializer = TaskSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = TaskSerializer(obj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskListApiView(APIView):
    def get(self, request, format=None):
        pid = request.GET.get('pid',None)
        print(pid)
        obj = Task.objects.filter(project=pid)
        serializer = TaskSerializer(obj, many=True)
        return Response(serializer.data)

class TaskCreateView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListApiView(APIView):
    def get(self, request, format=None):
        obj = Project.objects.all()
        serializer = ProjectSerializer(obj, many=True)
        return Response(serializer.data)

class ProjectCreateView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectApiView(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request,pk,format=None):
        obj = self.get_object(pk)
        serializer = ProjectSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = ProjectSerializer(obj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# sub-tasks
class SubTaskApiView(APIView):
    def get_object(self, pk):
        try:
            return SubTask.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request,pk,format=None):
        obj = self.get_object(pk)
        serializer = SubTaskSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = SubTaskSerializer(obj, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubTaskListApiView(APIView):
    def get(self, request, format=None):
        tid = request.GET.get('tid',None)
        obj = SubTask.objects.filter(task=tid)
        serializer = SubTaskSerializer(obj, many=True)
        return Response(serializer.data)

class SubTaskCreateView(APIView):
    def post(self, request, format=None):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)