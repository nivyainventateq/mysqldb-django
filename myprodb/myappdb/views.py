from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from myappdb.models import Logintb

class Test(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self,request,*args,**kwargs):
        data=Logintb()
        data.uname=request.POST.get('username')
        data.pwd=request.POST.get('password')
        data.save()
        return HttpResponse('<h1> Data Stored </h1>')

test=Test.as_view()
