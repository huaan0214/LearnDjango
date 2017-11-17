from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
def upLoadDB(request,name,age):
	p=Person.objects.create(name=name,age=int(age))
	return HttpResponse('<p>数据创建成功<p>')
def getDB(request):
	p=Person.objects.all()
	return render(request,'people/peopleDB.html',{"p":p})