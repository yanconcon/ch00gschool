from django.shortcuts import render,redirect
from staticWeb.forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login as auth_login ,logout

from staticWeb.models import News

# Create your views here.
from staticWeb.models import Student


def test(request):
    return render(request, 'y_plan.html')

def home(request):
    return render(request, 'home_base.html')

def news(request):
    return render(request, 'y_news.html')

def plan(request):
    return render(request, 'y_plan.html')

def peixun(request):
    return render(request, 'y_peixun_base.html')

def enterprise(request):
    return render(request, 'y_enterprise.html')

def recruitment(request):
    return render(request, 'y_recruitment.html')

def stu_signup(request):
	path=request.get_full_path()
	if request.method=='POST':
		form=SignupForm(data=request.POST,auto_id="%s")
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user=Student.objects.create_user(username=username,email=email,password=password)
			user.save()
			auth_user = authenticate(username=username,password=password)
			auth_login(request,auth_user)
			return redirect("home")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'x_signup.html',locals())

def uploadImg(request):
    if request.method == 'POST':
        new_img = News(
			content="aaaa",
            img=request.FILES.get('img'),
            title = request.FILES.get('img').name,
			is_show=True,
        )
        new_img.save()
    return render(request, 'upload.html')

def showImg(request):
    news = News.objects.all()
    for i in news:
        print (i.img.url)
    return render(request, 'show.html', locals())


