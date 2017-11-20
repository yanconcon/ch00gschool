from django.shortcuts import render,redirect
from staticWeb.forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login as auth_login ,logout
# Create your views here.

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

def signup(request):
	path=request.get_full_path()
	if request.method=='POST':
		form=SignupForm(data=request.POST,auto_id="%s")
		if form.is_valid():
			UserModel=get_user_model()
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user=UserModel.objects.create_user(username=username,email=email,password=password)
			user.save()
			auth_user = authenticate(username=username,password=password)
			auth_login(request,auth_user)
			return redirect("test")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'x_signup.html',locals())

