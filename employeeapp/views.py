from django.shortcuts import render
from employeeapp.forms import employeeform



def staticExample(request):
    return render(request,'static_example.html')


def employee_view(request):
    employee=employeeform()
    print(request.GET)

    if request.method == 'POST':
        employee=employeeform(request.POST)
        print(request.POST)

        if employee.is_valid():
             pass

    return render(request,'employee.html',{"employee":employee})



