from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from.froms import AddForm

# Create your views here.
def add(request):
	a=request.GET['a']
	b=request.GET['b']
	c=int(a)+int(b)
	return render(request,'calc/index.html',{'a':a,'b':b,'c':c})	
def add2(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))	
def home(request):
	return render(request,'calc/home.html')

def index(request):
	if request.method =='POST':
		form=AddForm(request.POST)
		
		if form.is_valid():
			a=form.cleaned_data['a']
			b=form.cleaned_data['b']
			c=str(int(a)+int(b))
			return render(request,'calc/index.html',{'a':a,'b':b,'c':c,'form':form})
	else:
		form=AddForm()
	return render(request,'calc/index.html',{'form':form})

def old_add2_redirect(request,a,b):
	return HttpResponseRedirect(reverse('add2',args=(a,b)))