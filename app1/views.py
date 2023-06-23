from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):                           # to get all
        Employees = Employee.objects.all()
        serializer = EmployeeSerializer(Employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   # added try-except within this 3 lines

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get(self, request, id):
        try:
            Employees = Employee.objects.get(id=id)

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(Employees)                       # removed many=True
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            Employees = Employee.objects.get(id=id)         # try-except copy as it is from get method

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(Employees, data=request.data)       # added Employees before data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            Employees = Employee.objects.get(id=id)         # all same of put only 1 change

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(Employees, data=request.data, partial=True)     # added partial=True

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            Employees = Employee.objects.get(id=id)         # try-except copy as it is from get method

        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        # snippet = self.get_object(pk)             # dont take this line
        # snippet.delete()
        Employees.delete()
        msg = {"msg": "deleted"}
        return Response(msg, status=status.HTTP_204_NO_CONTENT)