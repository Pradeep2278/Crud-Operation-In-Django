from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Datas

def home(request):
    mydata=Datas.objects.all()
    return render(request,'home.html',{'datas':mydata})

def addData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        Datas.objects.create(Name=name, Age=age, Email=email)
        mydata=Datas.objects.all()
        return redirect('home')
    return render(request,'home.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Datas  # Ensure this model exists

def updateData(request, id):  # Corrected function name
    mydata = get_object_or_404(Datas, id=id)
    
    if request.method == 'POST':
        mydata.Name = request.POST.get('name')
        mydata.Age = request.POST.get('age')
        mydata.Email = request.POST.get('email')

        mydata.save()  # Save the updated data
        return redirect('home')  # Redirect to home page

    return render(request, 'update.html', {'data': mydata})

def deleteData(request,id):
    mydata=Datas.objects.get(id=id)
    mydata.delete()
    return redirect('home')
