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
    url(r'^activate/(?P<code>\w+)$', views.activate),  # 注册时带有激活码的激活连接页面
    url(r'^change_password/(?P<code>\w+)$',views.password_change),  # 更改密码

    # url(r'^password_change/$', views.password_change, name='password_change'),
    # url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     'django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    # url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
