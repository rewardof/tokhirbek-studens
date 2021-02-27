from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path('create/', views.student_create_view, name='create'),
]