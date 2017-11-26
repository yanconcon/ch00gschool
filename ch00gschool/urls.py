"""ch00gschool URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from ch00gschool import settings
from staticWeb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$',views.test,),
    url(r'^news/$',views.news),
    url(r'^foreign_plan/$',views.plan),
    url(r'^improvment/$',views.peixun),
    url(r'^enterprise/$',views.enterprise),
    url(r'^recruitment/$',views.recruitment),
    url(r'^home/$',views.home,name="home"),
    url(r'^studentsignup/',views.test_signup),
    url(r'^enterprisesignup/',views.ent_signup),
    url(r'^studentlogin/',views.stu_login,name="studentlogin"),
    url(r'^enterpriselogin/', views.ent_login),
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
    url(r'^logout/', views.logout1, name= 'logout'),
    url(r'^userland/', views.complete),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
