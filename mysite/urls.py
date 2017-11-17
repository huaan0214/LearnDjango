
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_view
from calc import views as calc_view
from people import views as people_view
<<<<<<< HEAD
urlpatterns = [
		url(r'^db\/([a-z]*[A-Z]*)\/(\d+)\/*$',people_view.upLoadDB,name='home_db'),
		url(r'^getdb\/*$',people_view.getDB,name='get_db'),
=======
from blogs import views as blogs_view
urlpatterns = [
		url(r'^db\/([a-z]*[A-Z]*)\/(\d+)\/*$',people_view.upLoadDB,name='home_db'),
		url(r'^getdb\/*$',blogs_view.getDB,name='get_db'),
>>>>>>> origin/master
		url(r'^\/*$',learn_view.home,name='home_learn'),
		url(r'^calc\/*$',calc_view.home,name='home_calc'),
		url(r'^add\/(\d+)\/(\d+)\/*$',calc_view.old_add2_redirect),#
		url(r'^new_add\/(\d+)\/(\d+)\/*$',calc_view.add2,name='add2'),#
    url(r'^admin\/*', admin.site.urls),
    ]