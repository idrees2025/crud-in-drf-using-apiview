from django.urls import path
from crud_app import views

urlpatterns = [
    path('list/',views.StudentList.as_view()),
    path("detail/<int:pk>/", views.Studentdetail.as_view())
]
