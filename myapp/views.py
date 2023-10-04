from django.shortcuts import render, redirect, get_object_or_404
from .models import Studentdetail  
from.forms import StudentdetailForm

def Home(request):
    return render(request, 'home.html')

def thanks(request):
    return render(request, 'thanks.html')


def about(request):
    return render(request, 'about.html')

def images(request):
    return render(request, 'images.html')

def services(request):
    return render(request, 'services.html')

def delete(request):
    return render(request, 'delete.html')

def Admission(request):
    if request.method == "POST":
        # Get data from the form
        Id = request.POST.get('Id')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')
        nationality = request.POST.get('nationality')
        email = request.POST.get('email')
        institute = request.POST.get('institute')
        blood_group = request.POST.get('blood_group')

        # Create a Student object and save it
        student = Studentdetail(
            Id=Id,
            name=name,
            phone_number=phone_number,
            dob=dob,
            nationality=nationality,
            email=email,
            institute=institute,
            blood_group=blood_group
        )
        student.save()
        return redirect('thanks')

    return render(request, 'Admission.html')

def Display(request):
    students = Studentdetail.objects.all()
    return render(request, 'Display.html', {'students': students})



def view_student_detail(request, student_id):
    student = get_object_or_404(Studentdetail, Id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def search_student(request):
    query = request.GET.get('q')
    students = Studentdetail.objects.filter(name=query) if query else "Result not found"
    return render(request, 'searchbyname.html', {'students': students, 'query': query})




def edit_student(request, student_id):
    student = get_object_or_404(Studentdetail, Id=student_id)

    if request.method == 'POST':
        form = StudentdetailForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('Display')  
    else:
        form = StudentdetailForm(instance=student)

    return render(request, 'edit_student.html', {'student': student, 'form': form})

def delete(request, Id):
    students = Studentdetail.objects.filter(Id=Id)
    
    for student in students:
        student.delete()
    
    return redirect('Display')
