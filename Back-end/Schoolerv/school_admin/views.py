from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import TeaacherSerializer
from .models import Teacher


# Create your views here.
@api_view(['POST'])
def add_teacher(request):
    try:
        params = request.data
        email_exist = Teacher.objects.filter(email = params['email']).exists()
        if not email_exist:
            serialized_data = TeaacherSerializer(data = params)
            if serialized_data.is_valid():
                serialized_data.save()
                msg = 'Data added'
            else:
                msg = 'form not valid'
        else:
            msg = 'Email exists'
    except:
        msg = 'something went wrong'
    return JsonResponse({'message':msg})

@api_view(['GET']):
def get_teacherlist(request):
    teachers = Teacher.objects.all()
    serialized_data = TeaacherSerializer(teachers,many = True)
    return JsonResponse({'result':serialized_data.data}) 

