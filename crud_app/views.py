from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics
# Create your views here.

class StudentList(generics.ListCreateAPIView):    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class Studentdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializer
