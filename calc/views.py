from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def add(request):
	a=request.GET['a']
	b=request.GET['b']
	c=int(a)+int(b)
	return HttpResponse(str(c))	
def add2(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))	
def home(request):
	return render(request,'calc/home.html')

def old_add2_redirect(request,a,b):
	return HttpResponseRedirect(reverse('add2',args=(a,b)))