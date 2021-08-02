
# ------------------ App Imports -------------------------
from Student_App.models          import Student
from Student_App.api.serializers import (StudentSerializer,
                                        CountStudentSerializer,
                                        StatusStudentSerializer)

# ------------------ DRF Imports -------------------------
from rest_framework          import generics
from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# ----------------- concrete view classes --------------------
class StudentList(generics.ListCreateAPIView):
    """this will List all the Students"""
    queryset           = Student.objects.all()
    serializer_class   = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return super().get_queryset()


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """this will List Individual Students"""
    queryset           = Student.objects.all()
    serializer_class   = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
        
class TotalNumOfStudents(APIView):
    """This will calculate the total number of students """
    def get(self,request):
        total_no_of_students = Student.objects.all().count()
        serializer           = CountStudentSerializer({'total_no_of_students': total_no_of_students})
        return Response(serializer.data)


class StudentsStatus(APIView):
    """This will return total number of active & inactive students """
    def get(self,request):
        active_students        = Student.objects.all().filter(active=True).count()
        inactive_students      = Student.objects.all().filter(active=False).count()
        data                   = {
            'active_students': active_students,
            'inactive_students':inactive_students
        }
        serializer           = StatusStudentSerializer(data)
        return Response(serializer.data)

    
class StudentSearch(generics.ListAPIView):
    """This will Search for a students  """     
    serializer_class   = StudentSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Student.objects.filter(name__contains=name)

