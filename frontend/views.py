from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
import json
import base64
from io import BytesIO
from backend.models import Project
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    data = requests.get('https://task-manager-ufaber.herokuapp.com/api/all-projects/').json()
    return render(request,"frontend/index.html",{'data':data})

def project(request,pk):
    data = requests.get('https://task-manager-ufaber.herokuapp.com/api/project/'+str(pk)).json()
    params ={'pid':pk}
    task_data = requests.get('https://task-manager-ufaber.herokuapp.com/api/task/',params=params).json()
    return render(request,"frontend/project.html",{'data':data,'task_data':task_data})

def task(request,pk1,pk2):
    # params ={'pid':pk2}
    data = requests.get('https://task-manager-ufaber.herokuapp.com/api/task/'+str(pk2)).json()
    return render(request,"frontend/tasks.html",{'data':data})

def task_edit(request,pk1,pk2):
    data = {}
    data['id'] = pk2
    data['project'] = pk1
    if request.method == "POST":    
        name = request.POST['name']
        desc = request.POST['desc']
        sd = request.POST['sd']
        ed = request.POST['ed']
        if(name!=''):
            data['name'] = name
        if(desc!=''):
            data['desc'] = desc
        if(sd!=''):
            data['start_date'] = sd
        if(ed!=''):
            data['end_date'] = ed
        r = requests.put('https://task-manager-ufaber.herokuapp.com/api/task/'+str(pk2)+"/",data=data)
        return redirect('/project/'+str(pk1)+'/task/'+str(pk2))
    return render(request,"frontend/task_form.html",{'data':data})

def task_delete(request,pk1,pk2):
    data = requests.delete('https://task-manager-ufaber.herokuapp.com/api/task/'+str(pk2))
    return redirect('/project/'+str(pk1))


def task_create(request,pk):
    data = {}
    data['project'] = pk
    data['user'] = request.user.id
    if request.method == "POST":    
        name = request.POST['name']
        desc = request.POST['desc']
        sd = request.POST['sd']
        ed = request.POST['ed']
        if(name!=''):
            data['name'] = name
        if(desc!=''):
            data['desc'] = desc
        if(sd!=''):
            data['start_date'] = sd
        if(ed!=''):
            data['end_date'] = ed
        r = requests.post('https://task-manager-ufaber.herokuapp.com/api/task-add/',data=data)
        return redirect('/project/'+str(pk))
    return render(request,"frontend/task_create.html",{'data':data})

def project_create(request):
    data = {}
    if request.method == "POST":    
        name = request.POST['name']
        desc = request.POST['desc']
        sd = request.POST['sd']
        ed = request.POST['ed']
        if(name!=''):
            data['name'] = name
        if(desc!=''):
            data['desc'] = desc
        if(sd!=''):
            data['start_date'] = sd
        if(ed!=''):
            data['end_date'] = ed
        r = requests.post('https://task-manager-ufaber.herokuapp.com/api/project/',data=data)
        image = request.FILES.get('img',False)
        r = r.json()
        pk = r['id']
        obj = Project.objects.filter(id=pk).first()
        obj.image = image
        obj.save()
        return redirect('/')
    return render(request,"frontend/project_create.html",{'data':data})

def project_edit(request,pk):
    data = {}
    data['id'] = pk
    if request.method == "POST":    
        name = request.POST['name']
        desc = request.POST['desc']
        sd = request.POST['sd']
        ed = request.POST['ed']
        if(name!=''):
            data['name'] = name
        if(desc!=''):
            data['desc'] = desc
        if(sd!=''):
            data['start_date'] = sd
        if(ed!=''):
            data['end_date'] = ed
        r = requests.put('https://task-manager-ufaber.herokuapp.com/api/project/'+str(pk)+"/",data=data)
        image = request.FILES.get('img',False)
        if(image):
            obj = Project.objects.filter(id=pk).first()
            obj.image = image
            obj.save()
        return redirect('/project/'+str(pk))
    return render(request,"frontend/project_form.html",{'data':data})

def project_delete(request,pk):
    data = requests.delete('https://task-manager-ufaber.herokuapp.com/api/project/'+str(pk))
    return redirect('/')
