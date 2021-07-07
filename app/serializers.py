from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        Model = School
       # fields=('student_name','subject_name','marks')
        fields = '__all__'