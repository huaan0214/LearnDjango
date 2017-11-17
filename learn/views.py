#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	string='我在自强学习Django，用它来建网站'
	TutorialList=['HTML','CSS','JavaScript','Python','Django']
	info_dict={'site':'learning','content':'各种IT技术'}
	List=map(str,range(100))
	return render(request,'learn/home.html',{'string':string,'TutorialList':TutorialList,'info_dict':info_dict,'List':List})