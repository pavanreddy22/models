from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import School
from .serializers import Schoolserializer

class studentList(APIView):
    def get(self, request):
        student1= School.objects.all()
        serializer=Schoolserializer(student1,many=True)
        return Response(serializer.data)

    def post(self):
        pass