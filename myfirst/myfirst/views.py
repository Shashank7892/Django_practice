from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UserForm
from service.models import service

def homepage(request):
    servicesdata=service.objects.all().order_by('id')[1:4]
    data={
        'servicedata':servicesdata
    }
    return render(request,"index.html",data)

def aboutUs(req):
    if req.method=="GET":
        outs=req.GET.get('output')
    return render(req,'aboutus.html',{'ots':outs})

def gallery(req):
    return render(req,'gallery.html')

def contact(req):
    return render(req,'contact.html') 

def course(req):
    return HttpResponse("<b>welcome to myfirst Django project111</b>")

def aboutdata(req,aid):
    return HttpResponse(aid)

def coursedata(req,courseid):
    return HttpResponse(courseid)

#method 1 using only GET[]
def Userform(req):
    finalans=0
    try:
        n1=int(req.GET['num1'])
        n2=int(req.GET['num2'])
        finalans=n1+n2
    except:
        pass
    return render(req,'userform.html',{'output':finalans})

# method 2 using GET.get()
def Userform1(req):
    
    finalans=0
    data={}
    try:
        n1=int(req.GET.get('num1'))
        n2=int(req.GET.get('num2'))
        finalans=n1+n2
        data={'output1':finalans}
    except:
        pass
    return render(req,'userform1.html',data)

def postform(req):
    finalans=0
    try:
        n1=int(req.POST['num1'])
        n2=int(req.POST['num2'])
        finalans=n1+n2
        return redirect('/gallery/')
    except:
        pass
    return render(req,'postuser.html',{'output':finalans})

def postform1(req): 
    finalans=0
    fn=UserForm()
    data={'form':fn}
    try:
        if req.method=="POST":
            n1=int(req.POST.get('num1'))
            n2=int(req.POST.get('num2'))
            finalans=n1+n2
            data={'n1':n1,
                  'n2':n2,
                  'form':fn,
                  'output1':finalans}
            url='/about-us/?output={}'.format(finalans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(req,'postuser1.html',data)

def submitform(req):
    finalans=0
    data={}
    try:
        if req.method=="POST":
            n1=int(req.POST.get('num1'))
            n2=int(req.POST.get('num2'))
            finalans=n1+n2
            data={'n1':n1,
                  'n2':n2,
                  'output1':finalans}
            
            return HttpResponse(finalans)
    except:
        pass
    

def newsdetails(request,newsid):
    print(newsid)
    servicesdata=service.objects.get(id=newsid)
    data={
        'servicesdata':servicesdata
    }
    
    return render(request,"details.html",data)