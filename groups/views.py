from groups.models import Names, TeleGroups
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")
def contact(request):
    if request.method == "POST":
        yourname=request.POST.get("yourname")
        groupname=request.POST.get("groupname")
        groupdesc=request.POST.get("groupdesc")
        telegroups=TeleGroups(Yourname=yourname,Groupname=groupname,Groupdesc=groupdesc,times=datetime.today())
        telegroups.save()
        print("success!!")
    return render(request,'contact.html')
def telegram(request):
    obj=TeleGroups.objects.all()
    return render(request,"telegram.html",{'objects':obj})
def whatsapp(request):
    obj=TeleGroups.objects.all()
    return render(request,"whatsapp.html",{'objects':obj})