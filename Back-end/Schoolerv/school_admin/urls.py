from django.urls import path
from . import views


urlpatterns = [
path('addteacher',views.add_teacher),
path('teachers/list',views.get_teacherlist) 
]

