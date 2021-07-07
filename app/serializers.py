from rest_framework import serializers
from .models import School

class schoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
       # fields=('student_name','subject_name','marks')
        fields = '__all__'