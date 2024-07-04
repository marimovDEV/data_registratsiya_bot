from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('students',views.students,name='students'),
    path('lessons',views.lessons,name='lessons')
]
