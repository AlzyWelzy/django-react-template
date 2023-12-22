from django.urls import path, include
from .views import *

urlpatterns = [
    path("", StudentList.as_view(), name="student-list"),
]
