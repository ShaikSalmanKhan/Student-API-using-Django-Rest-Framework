from django.urls import path
from Student_App.api.views import (StudentList,
                                   StudentDetail,
                                   TotalNumOfStudents,
                                   StudentsStatus,
                                   StudentSearch)

urlpatterns = [
    path('', StudentList.as_view()),
    path('<int:pk>/', StudentDetail.as_view()),
    path('total/', TotalNumOfStudents.as_view()),
    path('status/', StudentsStatus.as_view()),
    path('search/<str:name>/', StudentSearch.as_view()),
]