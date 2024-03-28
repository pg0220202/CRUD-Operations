from django.shortcuts import render,  redirect
from .models import Student
from django.contrib import messages


# Create your views here.

def insert(request):
    students = Student.objects.all()


    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")

            Student.objects.create(Full_name=name, Email=email)

            messages.success(request, "Student added successfully")
            return redirect('insert')

        elif "update" in request.POST:
            i = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")

            new_student = Student.objects.get(id=i)
            new_student.Full_name = name
            new_student.Email = email
            new_student.save()
            messages.success(request, "Student data updated successfully")
            return redirect('insert')


        elif "delete" in request.POST:
            d = request.POST.get("id")
            new_student = Student.objects.get(id=d)
            new_student.delete()

            messages.success(request, "Student deleted successfully")
            return redirect('insert')


    context = {"students": students}
    return render(request, 'index.html', context=context)
