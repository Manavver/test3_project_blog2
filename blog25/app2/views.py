from django.shortcuts import render, get_object_or_404

from .models import Actoress


# Create your views here.

def Actoress_list(request):
    Ar=Actoress.objects.all()
    print(Ar)
    return render(request,'Actoress_list.html',{'Ar':Ar})

def Actoress_details(request, pk):
    Ard = get_object_or_404(Actoress, pk=pk)   # select * from Actoress where id/pk=4;
    print(Ard.Actoress_name)
    print(Ard.Actoress_des)
    return render(request, 'Actoress_details.html', {'Ard': Ard})