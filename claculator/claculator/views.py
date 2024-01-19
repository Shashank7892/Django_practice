from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import evenoddform

def calculator(request):
    finalans=0
    data={}
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            op=request.POSTs.get('opr')
            if op=="+":
                finalans=n1+n2
            elif op=="-":
                finalans=n1-n2
            elif op=="*":
                finalans=n1*n2
            elif op=="/":
                finalans=n1/n2
            
        data={"output":finalans}
    except:
        pass
    
            
    return render(request,"calculator.html",data)

def evenodd(request):
    en=evenoddform()
    data={"form":en}
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num"))
            if n1%2==0:
                c="even number"
            else:
                c="odd number"
                
            data={"form":en,
                  "out":c}
            
    except:
        pass
    return render(request,"evenodd.html",data)

def markssheet(request):
    data={}
    total=0
    per=''
    grade=''
    try:
        if request.method=="POST":
            s1=int(request.POST.get('sub1'))
            s2=int(request.POST.get('sub2'))
            s3=int(request.POST.get('sub3'))
            s4=int(request.POST.get('sub4'))
            s5=int(request.POST.get('sub5'))
            
            total=s1+s2+s3+s4+s5
            print(total)
            percentage=(total/500)*100
            print(percentage)
            per=str(percentage)+' '+'%'
            print(per)
            if percentage>90:
                grade="O"
            elif percentage>75 and percentage<=90:
                grade="A"
            elif percentage>60 and percentage<=75:
                grade="B"
            elif percentage>=35 and percentage<=60:
                grade="C"
            elif percentage<35:
                grade="Fail"
            
            data={'total':total,
                  'percentage':per,
                  'grade':grade}
    except:
        pass 
    return render(request,"markssheet.html",data)