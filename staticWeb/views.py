from django.shortcuts import render,redirect
from staticWeb.forms import SignupForm, LoginForm, Completion, Reset_emailForm, Change_passwordForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.http import HttpResponse
from staticWeb.models import News, Enterprise, Candidates, ActivateCode, MyUser
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
			user=Student.objects.create_user(username=username,email=email,password=password,role=role)
			auth_user = authenticate(username=username,password=password)

			# user.save()

			new_code = str(uuid.uuid4()).replace('-','')
			expire_time = timezone.now()+datetime.timedelta(2)
			code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
			code_record.save()

			active_link = 'http://%s/activate/%s' % (request.get_host(), new_code)
			active_email = '''点击<a href="%s">这里</a>激活''' % active_link
			send_mail(subject='测试激活邮件',
					  message='点击链接激活：%s' % active_link,
					  html_message=active_email,
					  from_email='m15992696532_1@163.com',
					  recipient_list=[email],
					  fail_silently=False)
			return render(request, 'success_hint.html', {'msg': '注册成功，请前往您的邮箱完成验证！'})

			# auth_login(request,auth_user)
			# return redirect("home")
	else:
		form=SignupForm(auto_id="%s")
	return render(request,'x_signup.html',locals())

def activate(request, code):
    query = ActivateCode.objects.filter(code=code,expire_timestamp__gte=timezone.now() )
    if query.count() > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return render(request, 'success_hint.html', {'msg':'激活成功', 'hint':'去登录', 'link': '/'})
    else:
        return render(request, 'success_hint.html', {'msg':'激活失败'})

def password_reset(request):
	path = request.get_full_path()
	if request.method == 'POST':
		form = Reset_emailForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			u = MyUser.objects.get(email = email)

			new_code = str(uuid.uuid4()).replace('-', '')
			expire_time = timezone.now() + datetime.timedelta(2)
			code_record = ActivateCode(owner=u, code=new_code, expire_timestamp=expire_time)
			code_record.save()

			active_link = 'http://%s/change_password/%s' % (request.get_host(), new_code)
			active_email = '''点击<a href="%s">这里</a>激活''' % active_link
			send_mail(subject='重置密码',
					  message='点击这里重置密码：%s' % active_link,
					  html_message=active_email,
					  from_email='m15992696532_1@163.com',
					  recipient_list=[email],
					  fail_silently=False)
			return render(request, 'registration/password_reset_done.html')
	else:
		form = Reset_emailForm(auto_id="%s")
	return render(request, 'registration/password_reset_form.html', locals())

def password_change(request,code):
	query = ActivateCode.objects.filter(code=code, expire_timestamp__gte=timezone.now())
	if query.count() > 0:
		code_record = query[0]
		user = code_record.owner
		if user is not None:
			path = request.get_full_path()
			if request.method == 'POST':
				form = Change_passwordForm(request.POST)
				if form.is_valid():
					password = form.cleaned_data['password']
					user.set_password(password)
					user.save()

					return render(request, 'registration/password_reset_complete.html')
			else:
				form = Change_passwordForm(auto_id="%s")
			return render(request, 'registration/password_reset_confirm.html', locals())
		else:
			return HttpResponse("无效验证码")



