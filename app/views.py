from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_dept(request):
    if request.method == 'POST':
        deptno= request.POST['dn']
        dname = request.POST['d']
        location = request.POST['loc']

        DO = Dept.objects.get_or_create( deptno = deptno ,dname=dname,location=location)[0]
        DO.save()
        return HttpResponse('dept is submited')
    return render(request,'insert_dept.html')

def insert_emp(request):
    DO = Dept.objects.all()
    d = {'DO':DO}
    if request.method == 'POST':
        deptno = request.POST['dp']
        DO = Dept.objects.get(deptno=deptno)
        DO.save()
        empno = request.POST['en']
        ename = request.POST['un']
        job = request.POST['jb']
        mgr = request.POST['mg']
        hiredate = request.POST['hd']
        salary = request.POST['sl']

        EO = Emp.objects.get_or_create(deptno= DO,empno=empno,ename=ename,job=job,mgr=mgr,hiredate=hiredate,salary=salary)[0]
        EO.save()
        return HttpResponse('Webpage is submited')
    return render(request,'insert_emp.html',d)

def retrieve_emp(request):
    DTO = Dept.objects.all()
    d = {'DTO':DTO}
    if request.method == 'POST':
        DS = request.POST.getlist('dp')
        eos = Emp.objects.none()
        for i in DS:
            eos = eos | Emp.objects.filter(deptno = i)
        d1 = {'eos': eos}
        return render(request,'display_emp.html',d1)
    return render(request,'retrieve_emp.html',d)
