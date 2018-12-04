from django.shortcuts import render
from studentapp.forms import studentform

def student_view(request):
    student=studentform()

    if request.method == 'POST':
        student=studentform(request.POST)

        if student.is_valid():
            pass

    return render(request,'student.html',{'student':student})
