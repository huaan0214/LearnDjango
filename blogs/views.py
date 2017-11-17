from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Article,Author,Tag
def getDB(request):
	A=Author.objects.all()
	At=Article.objects.all()
	T=Tag.objects.all()
	return render(request,'blogs/blogsDB.html',{"A":A,"At":At,'T':T})