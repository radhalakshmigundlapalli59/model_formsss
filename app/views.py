from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    form=TopicForm()
    d={'form':form}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('topic model is saved by modelforms')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    form=webpageForm()
    d={'form':form}
    if request.method=='POST':
        form_data=webpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('webpage model is saved by modelforms')
    return render(request,'insert_webpage.html',d)

def insert_acessrecords(request):
    form=AcessRecordsForm()
    d={'form':form}
    if request.method=='POST':
        form_data=AcessRecordsForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('acessrecords model is saved by modelforms')
    return render(request,'insert_acessrecords.html',d)