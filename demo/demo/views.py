from django.http import HttpResponse
from django.shortcuts import render

def homepage(req):
    data={
        'title':'homepage',
        'bdata':'Welcome to the page',
        'setdata':['php','java','python'],
        'studentd':[
            {'name':'shashank','phonenumber':'9740239342','course':'python'},
            {'name':'ajay','phonenumber':'9740239341','course':'php'},
            {'name':'vijay','phonenumber':'9740239343','course':'java'},
            {'name':'sujay','phonenumber':'9740239344','course':'c++'},
        ]
    }
    return render(req,"index.html",data)

def aboutus(req):
    return HttpResponse("<h1>welcome the page</h1>")

def course(req):
    return HttpResponse("this is a course page")

def coursedata(req,courseid):
    return HttpResponse(courseid)