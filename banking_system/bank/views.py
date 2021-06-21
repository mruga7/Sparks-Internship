from .models import Transfer,History
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"bank/Home.html")

# def customer(request):
#     return render(request,"bank/Customer-List.html")    
def info(request,id):
   

        return render(request,"bank/info.html",{

            "infolist":Transfer.objects.all().filter(id=id),
        
         })    
def info2(request):
   if request.method=="POST":
        Sender=request.POST.get('Name',False)
        Receiver=request.POST.get('email',False)
        Amount=request.POST.get('text',False)
        history=History(Sender=Sender,Receiver=Receiver,Amount=Amount)
        history.save()
        
        return render(request,"bank/Transaction-History.html",{
            "hi":History.objects.all()
        })          
    
def transaction(request):
    return render(request,"bank/Transaction-History.html")    

def transfer(request):
    return render(request,"bank/info.html") 

def userlist(request):
    return render(request,"bank/Customer-List.html",{    
    "userlist" : Transfer.objects.all()
    })



