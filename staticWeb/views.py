from django.shortcuts import render,redirect
from staticWeb.forms import SignupForm,LoginForm,Completion
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.http import HttpResponse
from staticWeb.models import News, Enterprise,Candidates
from django.core.mail import  send_mail
# Create your views here.
from staticWeb.models import Student
import uuid
from django.utils import timezone
import datetime



def test(request):
    return render(request, 'y_plan.html')

def home(request):
    news = News.objects.all()
    candicates = Candidates.objects.all()
    return render(request, 'home_base.html',locals())

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
			role = 'student'
			studentnews = News()
			user=Student.objects.create_user(username=username,email=email,password=password,role='student')
			user.save()
			auth_user = authenticate(username=username,password=password)
			auth_login(request,auth_user)
			return redirect("home")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'x_signup.html',locals())

def ent_signup(request):
	path=request.get_full_path()
	if request.method=='POST':
		form=SignupForm(data=request.POST,auto_id="%s")
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			role = 'enterprise'
			user=Enterprise.objects.create_user(username=username,email=email,password=password,role='enterprise')
			user.save()
			auth_user = authenticate(username=username,password=password)
			auth_login(request,auth_user)
			return redirect("home")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'x_signup.html',locals())


def stu_login(request):
	path = request.get_full_path()
	if request.method == 'POST':
		form = LoginForm(data=request.POST, auto_id="%s")
		if form.is_valid():
			data = form.clean()
			user = authenticate(username=data['username'].strip(), password=data['password'])
			auth_login(request, user)
			if request.user.role == "student":
				return redirect("home")
			elif request.user.role == "enterprise":
				return redirect("logout")

	else:
		form = LoginForm(auto_id="%s")

	return render(request, 'x_stu_login.html', locals())

def ent_login(request):
	path = request.get_full_path()
	if request.method == 'POST':
		form = LoginForm(data=request.POST, auto_id="%s")
		if form.is_valid():
			data = form.clean()
			user = authenticate(username=data['username'].strip(), password=data['password'])
			auth_login(request, user)
			if request.user.role == "enterprise":
				return redirect("home")
			elif request.user.role == "student":
				return redirect("logout")

	else:
		form = LoginForm(auto_id="%s")

	return render(request, 'x_ent_login.html', locals())



def uploadImg(request):
    if request.method == 'POST':
        new = News(
			content="aaaa",
            img=request.FILES.get('img'),
            title = request.FILES.get('img').name,
			is_show=True,
        )
        new.save()
    return render(request, 'upload.html')

def showImg(request):
    news = News.objects.all()
    for i in news:
        print (i.img.url)
    return render(request, 'show.html', locals())

def logout1(request):

    logout(request)
    
    return redirect('home')

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'x_userland.html', context)

def complete(request):
	if request.method=='POST':
		form=Completion(request.POST)
		if form.is_valid():
			stu_calss = form.cleaned_data['stu_calss']
			tele_num = form.cleaned_data['tele_num']
			user = request.user
			u1 = Student.objects.get_by_natural_key(username= user.username)
			u1.stu_class = stu_calss
			u1.tele_num = tele_num
			u1.save()

			return redirect("home")
	else:
		form=Completion(auto_id="%s")
	return render(request,'x_userland.html',{'form':form})

def test_signup(request):
	path=request.get_full_path()
	if request.method=='POST':
		form=SignupForm(data=request.POST,auto_id="%s")
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			role = 'student'
			studentnews = News()
			user=Student.objects.create_user(username=username,email=email,password=password,role='student')
			user.save()

			new_code = str(uuid.uuid4()).replace('-','')
			expire_time = timezone.now()+datetime.timedelta(day=2)
			code_record = uuid.(owner=user,code=new_code,expire_time=expire_time)
			code_record.save()
			auth_user = authenticate(username=username,password=password)
			auth_login(request,auth_user)
			return redirect("home")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'x_signup.html',locals())