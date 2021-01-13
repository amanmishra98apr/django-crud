from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse

# Create your views here.

# edit data
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print("id is", id)
        student = User.objects.get(pk=id)
        student_data = {"id": student.id, "name": student.name, "email":student.email, "password": student.password}
        return JsonResponse(student_data)
    else:
        return JsonResponse({"status": "error"})

# delete data
def delete_data(request):
    print("thi is delete data view")
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "failed"})


# insert data
def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')    
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if sid == "":
                usr = User(name=name, email=email, password=password)
                usr.save()
            else:
                usr = User(id=sid, name=name, email=email, password=password)
                usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            
            return JsonResponse({"status": "saved", 'student_data': student_data})
        else:
            return JsonResponse({"status": "failed"})
            


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'crud_app/home.html', {'form': form, 'stu': stud})
