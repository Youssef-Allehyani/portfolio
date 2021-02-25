from django.shortcuts import render
from .models import Work
from .models import Courses
import datetime
from django.shortcuts import render , get_object_or_404
# Create your views here.

def work (request):
    job = Work.objects
    coures = Courses.objects
    date = datetime.datetime.now()
    MyDate = date.strftime("%Y")
    myage = date.strftime("%y") 
    
    return render(request,'work/index.html',{"job":job,"Courses":coures,"MyDate":MyDate,"myage":myage})

def works_detail(request,works_id):
    work_detail = get_object_or_404( Work ,pk = works_id)
    return render ( request,'work/detail.html' , {'work': work_detail})

def coures_detail(request,coures_id):
    coures_detail = get_object_or_404( Courses ,pk = coures_id)
    return render ( request,'work/coures.html' , {'coures': coures_detail})


    