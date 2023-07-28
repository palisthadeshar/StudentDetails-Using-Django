from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Student
from .serializer import StudentSerilizers
from rest_framework import viewsets
from .forms import StudentForm
from django.http import JsonResponse


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    students = Student.objects.all()
    serializer_class = StudentSerilizers
    

@api_view(["GET"])
def get(request):
    student = Student.objects.all()
    serializer = StudentSerilizers(student,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def post(request):
    serializer = StudentSerilizers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PUT"])
def update(request, id:int):
    student = get_object_or_404(Student, id=id)
    print(student)
    serializer = StudentSerilizers(student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def delete_api(request, id:int):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return Response({"deleted data"})


def student_form(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            
            form.save()
            
            return redirect('studentdetails')
    
    form=StudentForm()
    return render(request,"studentdetailsform.html",{"form":form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'studentrecords.html', {'data': students})

def update_record(request, id:int):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST, instance=student)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('studentdetails')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_record.html', {'form': form})


def delete(request, id:int):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('studentdetails')
