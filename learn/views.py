#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
def sendMail(request):
	send_mail('测试测试测试', '这是测试用的 测试用的饿啊.', '1097634923@qq.com',['1289171009@qq.com'], fail_silently=False)
	return HttpResponse('发送OK')
def home(request):
	string='我在自强学习Django，用它来建网站'
	TutorialList=['HTML','CSS','JavaScript','Python','Django']
	info_dict={'site':'learning','content':'各种IT技术'}
	List=map(str,range(100))
	return render(request,'learn/home.html',{'string':string,'TutorialList':TutorialList,'info_dict':info_dict,'List':List})
