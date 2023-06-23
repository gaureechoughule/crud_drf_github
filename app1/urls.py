from django.urls import path
from .views import EmployeeList, EmployeeDetail

urlpatterns = [
    path("emp/", EmployeeList.as_view(), name="emp"),
    path('emp/<int:id>/', EmployeeDetail.as_view()),

]
