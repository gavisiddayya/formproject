from django.shortcuts import render
from testapp.models import Customer

# Create your views here.
def practice_view(request):
    ctr=Customer.objects.all()


    return render(request,'display.html',{'ctr':ctr})


