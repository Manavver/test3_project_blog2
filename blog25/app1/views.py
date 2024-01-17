from django.shortcuts import render, get_object_or_404, redirect

from .models import Actor


# Create your views here.

def Actor_list(request):
    A=Actor.objects.all()
    print(A)
    return render(request,'Actor_list.html',{'A':A})

def Actor_details(request, pk):
    Ad = get_object_or_404(Actor, pk=pk)   # select * from Actor where id/pk=4;
    print(Ad.Actor_name)
    print(Ad.Actor_des)
    return render(request, 'Actor_details.html', {'Ad': Ad})

def delete_actor(request, pk):
    obj = get_object_or_404(Actor, pk=pk)
    obj.delete()
    return redirect('/app1/Actors/')